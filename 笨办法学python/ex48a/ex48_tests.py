# -*- coding: utf-8 -*-
from nose.tools import *
from ex48.lexicon import lexicon

def test_directions():
	a=lexicon()
	assert_equal(a.scan("north"),[('direction','north')])
	b=lexicon()
	result=b.scan("north south east")
	assert_equal(result,[('direction','north'),('direction','south'),('direction','east')])
	
def test_verbs():
	a=lexicon()
	assert_equal(a.scan("go"), [('verb', 'go')])
	b=lexicon()
	result =b.scan("go kill eat")
	assert_equal(result, [('verb', 'go'),
						  ('verb', 'kill'),
						  ('verb', 'eat')])


def test_stops():
	a=lexicon()
	assert_equal(a.scan("the"), [('stop', 'the')])
	b=lexicon()
	result =b.scan("the in of")
	assert_equal(result, [('stop', 'the'),
						  ('stop', 'in'),
						  ('stop', 'of')])


def test_nouns():
	a=lexicon()
	assert_equal(a.scan("bear"), [('noun', 'bear')])
	b=lexicon()
	result =b.scan("bear princess")
	assert_equal(result, [('noun', 'bear'),
						  ('noun', 'princess')])

def test_numbers():
	a=lexicon()
	assert_equal(a.scan("1234"), [('number',1234)])
	b=lexicon()
	result =b.scan("3 91234")
	assert_equal(result, [('number',3),
						  ('number',91234)])


def test_errors():
	a=lexicon()
	assert_equal(a.scan("asdfadfasdf"), [('error', 'asdfadfasdf')])
	b=lexicon()
	result =b.scan("bear ias princess")
	assert_equal(result, [('noun', 'bear'),
						  ('error', 'ias'),
						  ('noun', 'princess')])