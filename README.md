# Wireless-Network-Expert-RAG

## Overview
This project involves:
1. Parsing wireless networking specifications from `.txt` and `.pdf` files.
2. Fine-tuning the **OPT** (Open Pre-trained Transformer) model for causal language modeling using parsed data.
3. Testing the fine-tuned model for text generation and question answering.
4. Implementing a pipeline for answering questions using **DistilBERT** fine-tuned on SQuAD.

---

## Features
- **Parsing Specifications**:
  - Reads `.txt` and `.pdf` files from the `wireless_specs/` directory.
  - Extracts and stores the text content for training purposes.
- **Fine-Tuning**:
  - Fine-tunes the `facebook/opt-125m` model on parsed wireless specifications for improved text generation capabilities.
- **Text Generation**:
  - Generates structured responses related to wireless networking using the fine-tuned model.
- **Question Answering**:
  - Uses `distilbert-base-uncased-distilled-squad` to provide answers to technical questions from a given context.

---

## Setup Instructions
