# -*- coding: utf-8 -*-
__author__ = 'panda'
import sys, os

ROOTDIR = os.path.join(os.path.dirname(__file__), os.pardir)
sys.path.append(os.path.join(ROOTDIR, "lib"))

# Set your own model path
MODELDIR=os.path.join(ROOTDIR, "ltp_data")

from pyltp import Segmentor, Postagger, Parser, NamedEntityRecognizer, SementicRoleLabeller

sentence = "中国进出口银行与中国银行加强合作"

segmentor = Segmentor()
segmentor.load(os.path.join(MODELDIR, "cws.model"))
words = segmentor.segment(sentence)
print "\t".join(words)

postagger = Postagger()
postagger.load(os.path.join(MODELDIR, "pos.model"))
postags = postagger.postag(words)
# list-of-string parameter is support in 0.1.5
# postags = postagger.postag(["中国","进出口","银行","与","中国银行","加强","合作"])
print "\t".join(postags)

parser = Parser()
parser.load(os.path.join(MODELDIR, "parser.model"))
arcs = parser.parse(words, postags)

print "\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs)

recognizer = NamedEntityRecognizer()
recognizer.load(os.path.join(MODELDIR, "ner.model"))
netags = recognizer.recognize(words, postags)
print "\t".join(netags)

labeller = SementicRoleLabeller()
labeller.load(os.path.join(MODELDIR, "srl/"))
roles = labeller.label(words, postags, netags, arcs)

for role in roles:
    print role.index, "".join(
            ["%s:(%d,%d)" % (arg.name, arg.range.start, arg.range.end) for arg in role.arguments])

segmentor.release()
postagger.release()
parser.release()
recognizer.release()
labeller.release()