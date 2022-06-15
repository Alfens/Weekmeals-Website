mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"your-email@domain.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[theme]\n\
primaryColor='#c19e9e'\n\
backgroundColor='#e7eacb'\n\
secondaryBackgroundColor='#e2d8b4'\n\
textColor='#1e2146'\n\
font='serif' \n\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
"> ~/.streamlit/config.toml

