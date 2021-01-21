mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"inderaihsan@yahoo.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = process.env.PORT || 3000\n\
" > ~/.streamlit/config.toml
