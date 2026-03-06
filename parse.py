"""
Simple command-line interface for resume parsing
"""

import sys
import json
from pathlib import Path
from universal_parser import parse_resume


def main():
    """Main CLI function"""
    
    if len(sys.argv) < 2:
        print("\n" + "="*80)
        print("UNIVERSAL RESUME PARSER")
        print("="*80)
        print("\nParse any resume format into AI-friendly structured text")
        print("\nSupported formats:")
        print("  • PDF (.pdf)")
        print("  • Word (.docx, .doc)")
        print("  • Text (.txt)")
        print("  • Images (.png, .jpg, .jpeg, .tiff, .bmp)")
        print("\nHandles:")
        print("  ✓ Tables")
        print("  ✓ Multi-column layouts")
        print("  ✓ Colored backgrounds")
        print("  ✓ Icons and images")
        print("  ✓ Complex formatting")
        print("\nUsage:")
        print("  python parse.py <file_path>")
        print("\nExamples:")
        print('  python parse.py "resume.pdf"')
        print('  python parse.py "resume.docx"')
        print('  python parse.py "screenshot.png"')
        print("\n" + "="*80 + "\n")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    print(f"\n{'='*80}")
    print(f"Parsing: {Path(file_path).name}")
    print(f"{'='*80}\n")
    
    # Parse
    print("⏳ Processing...")
    result = parse_resume(file_path)
    
    if result['success']:
        print("✅ SUCCESS!\n")
        
        # Display metadata
        metadata = result['metadata']
        text = result['text']
        
        print("📊 Metadata:")
        print(f"  • Format: {metadata.get('format', 'unknown')}")
        print(f"  • Method: {metadata.get('method', 'unknown')}")
        if 'pages' in metadata:
            print(f"  • Pages: {metadata['pages']}")
        if 'tables' in metadata:
            print(f"  • Tables: {metadata['tables']}")
        
        word_count = len(text.split())
        line_count = len(text.split('\n'))
        
        print(f"  • Words: {word_count}")
        print(f"  • Lines: {line_count}")
        print(f"  • Characters: {len(text)}")
        
        # Display preview
        print(f"\n📄 AI-Friendly Structured Text (first 1500 chars):")
        print("-" * 80)
        print(text[:1500])
        if len(text) > 1500:
            print("...")
        print("-" * 80)
        
        # Save outputs
        output_file = Path(file_path).stem + "_parsed.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"\n💾 Full text saved to: {output_file}")
        
        metadata_file = Path(file_path).stem + "_metadata.json"
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump({
                **metadata,
                'word_count': word_count,
                'line_count': line_count,
                'char_count': len(text)
            }, f, indent=2)
        print(f"💾 Metadata saved to: {metadata_file}")
        
        print(f"\n{'='*80}")
        print("✅ Ready for AI processing!")
        print("="*80)
        print("\nThis text is optimized for line-by-line AI reading:")
        print("  ✓ No duplicates")
        print("  ✓ Clear section markers")
        print("  ✓ Logical flow")
        print("  ✓ Clean formatting")
        print(f"{'='*80}\n")
        
    else:
        print(f"❌ FAILED")
        print(f"Error: {result['error']}\n")
        print(f"{'='*80}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
