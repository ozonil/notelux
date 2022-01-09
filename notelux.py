from app import app
from app.models import Info

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'info': info}