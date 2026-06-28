from core.cognition_loop import CognitionLoop

def test_cognition_pipeline():
    loop = CognitionLoop()
    result = loop.run('hello')
    assert 'perceive' in result
