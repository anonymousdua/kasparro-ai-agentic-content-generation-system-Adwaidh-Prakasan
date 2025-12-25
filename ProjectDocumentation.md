# Kasparro AI Agentic Content Generation System

## Table of Contents
1. [Overview](#overview)
2. [Architecture](#architecture)
3. [System Components](#system-components)
4. [Setup & Installation](#setup--installation)
5. [Usage](#usage)
6. [Project Structure](#project-structure)
7. [Agents](#agents)
8. [Logic Blocks](#logic-blocks)
9. [Output Files](#output-files)
10. [Troubleshooting](#troubleshooting)

---

## Overview

The **Kasparro AI Agentic Content Generation System** is an intelligent, multi-agent pipeline designed to automatically generate comprehensive product marketing content. It leverages the Groq API with the LLaMA 3.3 70B model to create diverse content types from raw product data.

### Key Features
- **Modular Agent Architecture**: Specialized agents handle different content generation tasks
- **AI-Powered Generation**: Uses advanced LLM capabilities for high-quality content
- **Structured Output**: Generates JSON-formatted outputs for easy integration
- **Scalable Pipeline**: Extensible design for adding new agents and content types

---

## Architecture

The system follows a **sequential pipeline architecture** where data flows through multiple agents in order:

```
Input Agent → Parser Agent → Question Agent → FAQ Agent → Product Page Agent → Comparison Agent
     ↓            ↓              ↓               ↓              ↓                   ↓
  Raw Data   Structured    Questions      FAQ Items    Product Page      Comparison
             Product Data   JSON           JSON           JSON              JSON
```

Each agent:
1. Receives the current state (including previous agent outputs)
2. Processes the data
3. Updates the state with new information
4. Returns the state to the next agent

---

## System Components

### Core Dependencies
- **groq**: Python SDK for Groq API interactions
- **python-dotenv**: Environment variable management for API keys

### Model Configuration
- **Model**: `llama-3.3-70b-versatile`
- **API**: Groq (high-speed LLM inference)
- **Temperature**: Set to 0 for deterministic outputs (where applicable)

---

## Setup & Installation

### Prerequisites
- Python 3.7 or higher
- Groq API key (obtain from [console.groq.com](https://console.groq.com))

### Step 1: Clone/Download Repository
```bash
# Navigate to project directory
cd kasparro-ai-agentic-content-generation-system-Adwaidh-Prakasan
```

### Step 2: Create Environment Variables
Create a `.env` file in the project root:
```
GROQ_API_KEY=your_groq_api_key_here
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Create Output Directory
```bash
mkdir outputs
```

### Step 5: Run the Pipeline
```bash
python run.py
```

Expected output:
```
All pages generated successfully.
```

---

## Usage

### Running the Pipeline

**Basic Execution:**
```bash
python run.py
```

### Modifying Product Data

Edit `agents/input_agent.py` to change the product information:

```python
def run():
    return {
        "raw_product_data": {
            "Product Name": "Your Product Name",
            "Concentration": "Your Concentration",
            "Skin Type": ["Type1", "Type2"],
            "Key Ingredients": ["Ingredient1", "Ingredient2"],
            "Benefits": ["Benefit1", "Benefit2"],
            "How to Use": "Usage instructions",
            "Side Effects": "Potential side effects",
            "Price": 999
        }
    }
```

---

## Project Structure

```
kasparro-ai-agentic-content-generation-system/
├── config.py                    # Configuration and API client
├── run.py                       # Entry point
├── requirements.txt             # Python dependencies
├── README.md                    # Quick start guide
├── ProjectDocumentation.md      # This file
│
├── agents/                      # Agent modules
│   ├── input_agent.py          # Supplies raw product data
│   ├── parser_agent.py         # Structures raw data
│   ├── question_agent.py       # Generates user questions
│   ├── faq_agent.py            # Creates FAQ content
│   ├── product_page_agent.py   # Generates product pages
│   └── comparison_agent.py     # Creates product comparisons
│
├── logic_blocks/               # Content generation functions
│   ├── benefits.py             # Benefits description
│   ├── usage.py                # Usage instructions
│   ├── ingredients.py          # Ingredients information
│   ├── safety.py               # Safety information
│   ├── pricing.py              # Price formatting
│   └── comparison.py           # Comparison logic
│
├── orchestrator/               # Pipeline orchestration
│   └── pipeline.py             # Main pipeline coordinator
│
└── outputs/                    # Generated output files
    ├── product_page.json       # Product page content
    ├── faq.json                # FAQ content
    └── comparison_page.json    # Comparison page content
```

---

## Agents

### 1. Input Agent (`agents/input_agent.py`)
**Purpose**: Provides raw product data  
**Output**: `state["raw_product_data"]`  
**Responsibility**: Define product information (can be hardcoded or from a database)

```python
{
    "Product Name": "GlowBoost Vitamin C Serum",
    "Concentration": "10% Vitamin C",
    "Skin Type": ["Oily", "Combination"],
    "Key Ingredients": ["Vitamin C", "Hyaluronic Acid"],
    "Benefits": ["Brightening", "Fades dark spots"],
    "How to Use": "Apply 2–3 drops in the morning before sunscreen",
    "Side Effects": "Mild tingling for sensitive skin",
    "Price": 699
}
```

### 2. Parser Agent (`agents/parser_agent.py`)
**Purpose**: Normalize and structure raw data  
**Input**: `state["raw_product_data"]`  
**Output**: `state["product"]`  
**Responsibility**: Convert raw data to a consistent internal format

```python
{
    "name": "GlowBoost Vitamin C Serum",
    "concentration": "10% Vitamin C",
    "skin_type": ["Oily", "Combination"],
    "ingredients": ["Vitamin C", "Hyaluronic Acid"],
    "benefits": ["Brightening", "Fades dark spots"],
    "usage": "Apply 2–3 drops in the morning before sunscreen",
    "side_effects": "Mild tingling for sensitive skin",
    "price": 699
}
```

### 3. Question Agent (`agents/question_agent.py`)
**Purpose**: Generate categorized user questions about the product  
**Input**: `state["product"]`  
**Output**: `state["questions"]`  
**Model**: LLaMA 3.3 70B with structured JSON prompt  
**Categories**: Informational, Usage, Safety, Purchase, Comparison

**Sample Output:**
```json
{
  "Informational": [
    "What is the concentration of Vitamin C in this serum?",
    "Is this serum suitable for all skin types?"
  ],
  "Usage": [
    "How much product should I use per application?",
    "Can I use this serum with other products?"
  ],
  "Safety": [
    "Are there any side effects?",
    "Is it safe for sensitive skin?"
  ],
  "Purchase": [
    "What is the price of this serum?",
    "Is there a guarantee?"
  ],
  "Comparison": [
    "How does this compare to other Vitamin C serums?",
    "What makes this product unique?"
  ]
}
```

### 4. FAQ Agent (`agents/faq_agent.py`)
**Purpose**: Create FAQ content from product data  
**Input**: `state["product"]`  
**Output**: `outputs/faq.json`  
**Responsibility**: Use logic blocks to generate answers

**Output Format:**
```json
{
  "page": "FAQ",
  "items": [
    {
      "q": "What does this serum do?",
      "a": "This serum helps with Brightening, Fades dark spots."
    },
    {
      "q": "How do I use it?",
      "a": "Apply 2–3 drops in the morning before sunscreen"
    }
  ]
}
```

### 5. Product Page Agent (`agents/product_page_agent.py`)
**Purpose**: Generate complete product page content  
**Input**: `state["product"]`  
**Output**: `outputs/product_page.json`  
**Responsibility**: Orchestrate logic blocks to create product page

**Output Format:**
```json
{
  "name": "GlowBoost Vitamin C Serum",
  "description": "This serum helps with Brightening, Fades dark spots.",
  "ingredients": ["Vitamin C", "Hyaluronic Acid"],
  "usage": "Apply 2–3 drops in the morning before sunscreen",
  "price": "₹699"
}
```

### 6. Comparison Agent (`agents/comparison_agent.py`)
**Purpose**: Create product comparison content  
**Input**: `state["product"]`  
**Output**: `outputs/comparison_page.json`  
**Responsibility**: Compare current product with similar products

---

## Logic Blocks

Logic blocks are utility functions that generate specific content components using product data.

### benefits.py
Generates product benefit descriptions.
```python
def benefits_block(product):
    return f"This serum helps with {', '.join(product['benefits'])}."
```

### usage.py
Returns product usage instructions.
```python
def usage_block(product):
    return product["usage"]
```

### ingredients.py
Lists product ingredients.

### safety.py
Provides safety and side effect information.

### pricing.py
Formats and displays pricing information.

### comparison.py
Handles product comparison logic.

---

## Output Files

All generated content is saved to the `outputs/` directory in JSON format:

### 1. `outputs/product_page.json`
Complete product marketing page content including name, description, ingredients, usage, and price.

### 2. `outputs/faq.json`
Frequently asked questions with answers, organized by common product inquiries.

### 3. `outputs/comparison_page.json`
Side-by-side comparison of the product with competing alternatives.

---

## Troubleshooting

### JSONDecodeError in Question Agent
**Error**: `json.decoder.JSONDecodeError: Expecting value: line 1 column 1`

**Solution**: 
- Ensure your Groq API key is valid
- Check internet connectivity
- The prompt now includes explicit formatting instructions

### FileNotFoundError for outputs directory
**Error**: `FileNotFoundError: [Errno 2] No such file or directory: 'outputs/faq.json'`

**Solution**:
```bash
mkdir outputs
```

### Missing API Key
**Error**: `GROQ_API_KEY not set in environment`

**Solution**:
1. Create a `.env` file in the project root
2. Add: `GROQ_API_KEY=your_key_here`
3. Run: `python run.py`

### Rate Limiting from Groq API
**Error**: API returns 429 status code

**Solution**:
- Add delays between requests
- Check your Groq API plan limits
- Reduce request frequency

### Python Not Found
**Error**: `python: command not found`

**Solution**:
```bash
# Use python3 if python is not available
python3 run.py

# Or set up an alias
alias python=python3
```

---

## Configuration Reference

### `config.py`
```python
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
MODEL = "llama-3.3-70b-versatile"
```

### Environment Variables
| Variable | Required | Description |
|----------|----------|-------------|
| `GROQ_API_KEY` | Yes | Your Groq API authentication key |

---

## API Response Format

All agents communicate through a shared `state` dictionary:

```python
state = {
    "raw_product_data": {...},      # From Input Agent
    "product": {...},                # From Parser Agent
    "questions": {...},              # From Question Agent
    "faq": {...},                    # From FAQ Agent
    # Outputs also written to JSON files
}
```

---

## Best Practices

1. **API Key Security**: Never commit `.env` files to version control
2. **Error Handling**: The system includes error handling with debugging output
3. **Scalability**: To add new agents, create a new file in `agents/` and import it in `pipeline.py`
4. **Testing**: Modify `input_agent.py` to test with different product data
5. **Output Validation**: Check JSON files in `outputs/` to verify quality

---

## Future Enhancements

- [ ] Database integration for product data
- [ ] Webhook support for real-time generation
- [ ] Multi-language content generation
- [ ] Template-based output customization
- [ ] Analytics and performance metrics
- [ ] Batch processing for multiple products
- [ ] User feedback integration
- [ ] Content caching and versioning

---

## Support & Contribution

For issues or contributions:
1. Check the troubleshooting section
2. Verify API key and dependencies
3. Review output files for validation
4. Test with different product data

---

## License & Attribution

**Project**: Kasparro AI Agentic Content Generation System  
**Developer**: Adwaidh Prakasan  
**Created**: December 2025

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | Dec 2025 | Initial release with 6 agents, JSON output support, and error handling |

---

*Last Updated: December 25, 2025*
