# Universal Resume Parser

Production-ready parser that outputs AI-friendly structured text from any resume format.

## 🎯 Key Features

- ✅ **Multi-format support**: PDF, DOCX, DOC, TXT, Images
- ✅ **Complex layout handling**: Tables, multi-column, nested columns
- ✅ **Colored backgrounds**: Advanced image preprocessing
- ✅ **AI-optimized output**: Line-by-line readable structured text
- ✅ **No duplicates**: Intelligent duplicate detection
- ✅ **Section markers**: Clear markers for AI understanding
- ✅ **Production-ready**: Error handling, logging, metadata

## 🚀 Quick Start

### Installation

```bash
pip install -r requirements.txt
```

**For image support**, also install Tesseract OCR:
- Windows: https://github.com/UB-Mannheim/tesseract/wiki
- macOS: `brew install tesseract`
- Linux: `sudo apt-get install tesseract-ocr`

### Usage

```bash
python parse.py "resume.pdf"
```

## 📝 Examples

### Parse PDF
```bash
python parse.py "resume.pdf"
```

### Parse DOCX
```bash
python parse.py "resume.docx"
```

### Parse Image/Screenshot
```bash
python parse.py "resume_screenshot.png"
```

## 💻 Python Integration

```python
from universal_parser import parse_resume

# Parse any format
result = parse_resume('resume.pdf')

if result['success']:
    # Get AI-friendly structured text
    text = result['text']
    
    # Send to Gemini/Claude
    structured_data = ai_extract(text)
```

## 📊 Output Format

### AI-Friendly Structured Text

The parser outputs text optimized for AI line-by-line reading:

```
=== CONTACT ===
John Doe
john.doe@email.com
(555) 123-4567

=== EXPERIENCE ===
Senior Software Engineer
Tech Corp | 2020-2023
- Led development of microservices
- Managed team of 5 developers

=== EDUCATION ===
BS Computer Science
University ABC | 2016-2020

=== SKILLS ===
Python, JavaScript, React, Docker, AWS

=== REFERENCES ===
Jane Smith
Manager at Tech Corp
Phone: (555) 987-6543
Email: jane.smith@techcorp.com
```

### Response Format

```python
{
    'success': True,
    'text': 'AI-friendly structured text...',
    'metadata': {
        'format': 'pdf',
        'pages': 2,
        'method': 'layout_aware',
        'word_count': 350,
        'line_count': 65
    }
}
```

## 🎓 Why This Format is Perfect for AI

### Line-by-Line Reading

AI models read text sequentially. Our format ensures:

1. **Clear section markers**: `=== SECTION ===` helps AI identify sections
2. **No duplicates**: Each piece of information appears once
3. **Logical flow**: Content flows naturally top to bottom
4. **Clean text**: No visual formatting that confuses AI
5. **Structured data**: Tables and lists formatted clearly

### Example: AI Understanding

**Input text:**
```
=== REFERENCES ===
Harumi Kobayashi Bailey Dupont
Wardiere Inc. / CEO Wardiere Inc. / CEO
Phone: 123-456-7890 Phone: 123-456-7890
```

**AI extracts:**
```json
{
  "references": [
    {
      "name": "Harumi Kobayashi",
      "company": "Wardiere Inc.",
      "title": "CEO",
      "phone": "123-456-7890"
    },
    {
      "name": "Bailey Dupont",
      "company": "Wardiere Inc.",
      "title": "CEO",
      "phone": "123-456-7890"
    }
  ]
}
```

## 🔧 Handles Complex Formats

### Tables
- Extracts and formats tables clearly
- Preserves structure for AI understanding

### Multi-Column Layouts
- Detects column boundaries
- Outputs in logical reading order

### Colored Backgrounds
- Image enhancement for better OCR
- Contrast adjustment
- Background removal

### Icons and Images
- Ignores decorative elements
- Focuses on text content

### Nested Columns
- Handles columns within columns
- Maintains logical flow

## 📁 Output Files

Running `python parse.py "resume.pdf"` creates:

1. **resume_parsed.txt** - Full AI-friendly structured text
2. **resume_metadata.json** - Metadata and statistics

## 🎯 POC1 Integration

```python
from universal_parser import parse_resume

def process_resume_for_poc1(file_path):
    """Process resume for POC1 workflow"""
    
    # Step 1: Parse resume
    result = parse_resume(file_path)
    
    if not result['success']:
        return {'error': result['error']}
    
    # Step 2: Get structured text
    raw_text = result['text']
    
    # Step 3: Send to Gemini/Claude for extraction
    structured_data = gemini_extract(raw_text)
    
    # Step 4: Continue with skill normalization, validation, etc.
    return {
        'raw_text': raw_text,
        'structured_data': structured_data,
        'metadata': result['metadata']
    }
```

## ✅ Benefits

| Feature | Benefit |
|---------|---------|
| No Duplicates | Lower token cost, clearer data |
| Section Markers | AI easily identifies sections |
| Clean Text | Better AI extraction quality |
| Logical Flow | Natural reading order |
| Multi-format | Handle any resume type |

## 🔍 Supported Formats

| Format | Extension | Status |
|--------|-----------|--------|
| PDF | .pdf | ✅ Full support |
| Word | .docx | ✅ Full support |
| Legacy Word | .doc | ✅ Supported |
| Text | .txt | ✅ Full support |
| PNG | .png | ✅ With Tesseract |
| JPEG | .jpg, .jpeg | ✅ With Tesseract |
| TIFF | .tiff | ✅ With Tesseract |
| BMP | .bmp | ✅ With Tesseract |

## 📚 Documentation

- `README.md` - This file
- `universal_parser.py` - Main parser implementation
- `parse.py` - Command-line interface

## 🎉 Summary

This parser is specifically designed for AI/LLM processing:

- ✅ Outputs text that AI can read line by line
- ✅ No visual formatting (AI doesn't need it)
- ✅ Clear section markers for understanding
- ✅ No duplicate content
- ✅ Handles all resume formats and complexities
- ✅ Production-ready with error handling

**Perfect for POC1 integration with Gemini/Claude!**
