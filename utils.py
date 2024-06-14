import re
import os
import pandas as pd
import spacy
import pytextrank
import nltk
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
from datasets import load_dataset

def generate_reference_file(dataset, model_path, column, output_file):
    model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    with open(output_file, 'w') as f:
        for index, row in dataset.iterrows():
            article = row[column]
            
            # Generate summary for each article
            inputs = tokenizer(article, padding=True, max_length=1024, truncation=True, return_tensors="pt")
            outputs = model.generate(**inputs)
            summary = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
            
            # Write the summary to the output file
            f.write(summary + "\n")


def extract_abstract(example):
    return {"abstract": example["article"].split('\n')[0]}

def select_top_sentences(example, column, nlp, tokenizer, limit_tokens=1024):
    # Process the text with spaCy and PyTextRank
    text = example[column]
    doc = nlp(text)

    # Generate the summary using pytextrank's built-in extractive summarization
    summary_sentences = [sent for sent in doc._.textrank.summary(limit_sentences=1000)]
    
    # Calculate token lengths for each summary sentence
    sent_token_lengths = [len(tokenizer.tokenize(sent.text)) for sent in summary_sentences]
    
    # Select top relevant sentences that fit within the token limit
    selected_sentences = []
    current_token_count = 0
    
    for sent, token_length in zip(summary_sentences, sent_token_lengths):
        if current_token_count + token_length <= limit_tokens:
            selected_sentences.append(sent.text)
            current_token_count += token_length
        else:
            break
    
    # Concatenate the selected sentences into a single text
    whole_text = ' '.join(selected_sentences)

    return {f"{column}-textrank": whole_text}

def select_top_sentences_by_sections(example, column, nlp, tokenizer, limit_tokens=1024):
    sections = example[column].split('\n')

    # Compute maximum number of tokens allowed per section
    section_token_limit = limit_tokens // len(sections)
    
    selected_sentences = []
    for section in sections:
        doc = nlp(section)
        
        # Generate the summary using pytextrank's built-in extractive summarization
        summary_sentences = [sent for sent in doc._.textrank.summary(limit_sentences=500)]
        
        # Calculate token lengths for each summary sentence
        sent_token_lengths = [len(tokenizer.tokenize(sent.text)) for sent in summary_sentences]
        
        current_token_count = 0
        for sent, token_length in zip(summary_sentences, sent_token_lengths):
            if current_token_count + token_length <= section_token_limit:
                selected_sentences.append(sent.text)
                current_token_count += token_length
            else:
                break

    # Concatenate the selected sentences into a single text
    whole_text = ' '.join(selected_sentences)

    return {f"{column}-textrank-bysections": whole_text}

def remove_references(example):
    # Pattern to match text within parentheses
    pattern = re.compile(r'\(.*?\)')
    
    return {"article_norefs": pattern.sub('', example['article'])}