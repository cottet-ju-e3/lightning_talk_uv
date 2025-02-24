# Fast API Demo
## Init Project
```shell
rm -rf ./uv-demo # clear
uv init uv-demo # uv init
cd uv-demo 
uv add fastapi uvicorn # Add fastapi dependency
cp -r ../demo_sources/src/ ./src/ # init with real sources
```

## Add build std config
```toml
[tool.hatch.build.targets.wheel]
packages = ["src/uv_demo"]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project.scripts]
main = "uv_demo.main:main"
```

## Start web app
```shell
uv run main
curl -X GET "localhost:5000/items/" | jq
```