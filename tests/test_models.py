from pathlib import Path
import xml.etree.ElementTree as ET
from app import Board
def test_bpmn_references_are_resolvable():
    root=ET.parse(Path(__file__).resolve().parents[1]/'docs/question-process.bpmn').getroot();ids={e.get('id') for e in root.iter() if e.get('id')}
    for e in root.iter():
        if e.tag.endswith('sequenceFlow'):assert e.get('sourceRef') in ids and e.get('targetRef') in ids
def test_restart_retains_committed_question(tmp_path):
    path=tmp_path/'persistent.db';b=Board(path);qid=b.submit(dict(room='R1',author='Example',text='Keep me',request_id='persist-001'))['id'];b.vote(dict(question_id=qid,voter_id='voter-0001'))
    fresh=Board(path);assert fresh.listing()[0]['text']=='Keep me';assert fresh.listing()[0]['votes']==1
