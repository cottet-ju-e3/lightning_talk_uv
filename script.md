rm -rf ./uv-demo
uv init uv-demo
cd uv-demo
uv add fastapi uvicorn
cp -r ../demo_sources/src/ ./src/

[tool.hatch.build.targets.wheel]
packages = ["src/uv_demo"]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project.scripts]
main = "uv_demo.main:main"

# Start web app
uv run main

curl -X GET "localhost:5000/items/" | jq


rm -rf /tmp/lightning_talk_uv && git clone git@github.com:cottet-ju-e3/lightning_talk_uv.git /tmp/lightning_talk_uv && cd /tmp/lightning_talk_uv/uv-demo && uv run main

# Run script with dependencies
uv run --no-project demo_sources/script.py
uv run --with rich --with requests demo_sources/script.py

uv add --script demo_sources/script.py requests rich

uv run demo_sources/script.py