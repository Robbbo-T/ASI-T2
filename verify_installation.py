#!/usr/bin/env python3
"""
Installation verification script for ASI-T2 repository dependencies.
Run this script after installing requirements to verify all dependencies are working.
"""
import sys
import importlib

def test_import(module_name, description=""):
    """Test importing a module and report status."""
    try:
        module = importlib.import_module(module_name)
        version = getattr(module, '__version__', 'unknown')
        print(f"✓ {module_name} ({version}) - {description}")
        return True
    except ImportError as e:
        print(f"❌ {module_name} - {description}: {e}")
        return False

def main():
    """Main verification function."""
    print("🔧 ASI-T2 Dependencies Verification")
    print("=" * 50)
    
    success = True
    
    # Core web framework
    print("\n📡 Web Framework Dependencies:")
    success &= test_import("fastapi", "FastAPI web framework")
    success &= test_import("uvicorn", "ASGI server")
    success &= test_import("pydantic", "Data validation")
    success &= test_import("starlette", "ASGI toolkit")
    
    # HTTP and requests
    print("\n🌐 HTTP Client Dependencies:")
    success &= test_import("requests", "HTTP requests library")
    
    # Data processing
    print("\n📊 Data Processing Dependencies:")
    success &= test_import("jsonschema", "JSON Schema validation")
    success &= test_import("yaml", "YAML parser")
    
    # XML processing
    print("\n🔒 XML Processing Dependencies:")
    success &= test_import("defusedxml", "Secure XML parsing")
    
    # Test key functionality
    print("\n🧪 Functionality Tests:")
    try:
        from fastapi import FastAPI
        from pydantic import BaseModel
        app = FastAPI(title="Test")
        class TestModel(BaseModel):
            name: str
        print("✓ FastAPI app creation works")
        
        from jsonschema import Draft202012Validator
        validator = Draft202012Validator({"type": "object"})
        print("✓ JSON Schema validator works")
        
        import defusedxml.ElementTree as ET
        root = ET.fromstring("<test>content</test>")
        print("✓ DefusedXML parsing works")
        
    except Exception as e:
        print(f"❌ Functionality test failed: {e}")
        success = False
    
    print("\n" + "=" * 50)
    if success:
        print("🎉 All dependencies verified successfully!")
        print("✅ Ready to run ASI-T2 applications")
        return 0
    else:
        print("💥 Some dependencies failed verification")
        print("❗ Please check the installation and try again")
        return 1

if __name__ == "__main__":
    sys.exit(main())