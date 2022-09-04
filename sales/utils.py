import uuid

def generate_code():
    code = str(uuid.uuid4()).upper().replace('-', '')[:12]
    return code