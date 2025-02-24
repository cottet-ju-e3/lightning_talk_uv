# lightning_talk_uv

## Demo
### Install uv
#### macOS and Linux
Use curl to download the script and execute it with sh:
```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### Windows
Use irm to download the script and execute it with iex:
```shell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Fast API Demo
#### Init Project
```shell
rm -rf ./uv-demo # clear
uv init uv-demo # uv init
cd uv-demo 
uv add fastapi uvicorn # Add fastapi dependency
cp -r ../demo_sources/src/ ./src/ # init with real sources
```

#### Add build std config
```toml
[tool.hatch.build.targets.wheel]
packages = ["src/uv_demo"]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project.scripts]
main = "uv_demo.main:main"
```

#### Start web app
```shell
uv run main
curl -X GET "localhost:5000/items/" | jq
```

```shell
rm -rf /tmp/lightning_talk_uv && git clone git@github.com:cottet-ju-e3/lightning_talk_uv.git /tmp/lightning_talk_uv && cd /tmp/lightning_talk_uv/uv-demo && uv run main
```
