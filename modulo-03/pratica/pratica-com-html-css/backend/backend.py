from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(
        use_reloader=False,
        use_debugger=False,
        passthrough_errors=True,
    )
