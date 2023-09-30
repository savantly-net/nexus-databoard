# find and replace the following line in /app/.streamlit/config.toml

toFind=^toolbarMode.*$
toReplace='toolbarMode = "minimal"'

sed -i "s/$toFind/$toReplace/g" /app/.streamlit/config.toml

# Add client script to streamlit static assets
streamlit_package_dir=$(python -m pip show streamlit | grep Location | sed 's/Location: \(.*\)/\1/')
jspath="${streamlit_package_dir}"/streamlit/static/static/js/
streamlitjs=$(find "${jspath}" -name main.*.js | head -1)
cat /app/docker/client-script.js >> "${streamlitjs}"

# Run the app
exec "$@"
