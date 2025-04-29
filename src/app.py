# app.py
from config.app import App
    
if __name__ == "__main__":
    app = App.get_app('development')
    # Choose how to run
    use_socketio = False

    if use_socketio:
        app.run_with_socketio()
    else:
        app.run_app()