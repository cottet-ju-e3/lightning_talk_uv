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

uv run main

curl -X GET "localhost:5000/items/" | jq