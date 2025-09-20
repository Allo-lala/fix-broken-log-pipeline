
cat > run-tests.sh << 'EOF'
#!/bin/bash
cd "${PWD}"
python -m pytest tests/test_outputs.py -v
EOF