# Wireless-Network-Expert-RAG

Wireless Specifications Parsing and Fine-Tuning Project
Overview
This project involves:

Parsing wireless networking specifications from .txt and .pdf files.
Fine-tuning the OPT (Open Pre-trained Transformer) model for causal language modeling using parsed data.
Testing the fine-tuned model for text generation and question answering.
Implementing a pipeline for answering questions using DistilBERT fine-tuned on SQuAD.
Features
Parsing Specifications:
Reads .txt and .pdf files from the wireless_specs/ directory.
Extracts and stores the text content for training purposes.
Fine-Tuning:
Fine-tunes the facebook/opt-125m model on parsed wireless specifications for improved text generation capabilities.
Text Generation:
Generates structured responses related to wireless networking using the fine-tuned model.
Question Answering:
Uses distilbert-base-uncased-distilled-squad to provide answers to technical questions from a given context.
