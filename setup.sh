#!/bin/bash

# Nairobi Road Encroachment Mapping System - Setup Script
# This script helps you set up the project quickly

echo "======================================================"
echo "  Nairobi Road Encroachment Mapping System"
echo "  Setup Script"
echo "======================================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python found: $(python3 --version)"
echo ""

# Check Python version
PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
REQUIRED_VERSION="3.8"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then 
    echo "❌ Python version must be >= 3.8. You have $PYTHON_VERSION"
    exit 1
fi

echo "✅ Python version check passed"
echo ""

# Ask if user wants to create virtual environment
read -p "Do you want to create a virtual environment? (recommended) [y/n]: " create_venv

if [ "$create_venv" = "y" ] || [ "$create_venv" = "Y" ]; then
    echo ""
    echo "Creating virtual environment..."
    python3 -m venv venv
    
    echo "✅ Virtual environment created"
    echo ""
    echo "Activating virtual environment..."
    
    # Activate based on OS
    if [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
        source venv/Scripts/activate
    else
        source venv/bin/activate
    fi
    
    echo "✅ Virtual environment activated"
fi

echo ""
echo "Installing dependencies..."
echo "This may take a few minutes..."
echo ""

pip install --upgrade pip
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ All dependencies installed successfully!"
else
    echo ""
    echo "❌ Error installing dependencies. Please check the error messages above."
    exit 1
fi

echo ""
echo "======================================================"
echo "  Setup Complete! 🎉"
echo "======================================================"
echo ""
echo "To run the application:"
echo ""
if [ "$create_venv" = "y" ] || [ "$create_venv" = "Y" ]; then
    if [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
        echo "  1. Activate virtual environment: venv\\Scripts\\activate"
    else
        echo "  1. Activate virtual environment: source venv/bin/activate"
    fi
fi
echo "  2. Run: streamlit run app.py"
echo ""
echo "Your browser will automatically open to http://localhost:8501"
echo ""
echo "For deployment instructions, see DEPLOYMENT.md"
echo "For quick start guide, see QUICKSTART.md"
echo ""
