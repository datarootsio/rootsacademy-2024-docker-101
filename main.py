from dagster import asset, Definitions


@asset
def hello_world() -> None:
    print("Hello world")


@asset
def hello_world_2() -> None:
    hello_world()
    print("Hello world 2")


definitions = Definitions(assets=[hello_world_2, hello_world])
print(definitions)
