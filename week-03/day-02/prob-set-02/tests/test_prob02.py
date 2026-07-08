from prob02 import process_performance_requests


def test_prob02():
    assert process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]) == ['Music', 'Dance', 'Drama']
    assert process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]) == ['Concert', 'Stand-up Comedy', 'Poetry', 'Magic Show']
    assert process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]) == ['Keynote Speech', 'Panel Discussion', 'Film Screening', 'Workshop', 'Art Exhibition']
