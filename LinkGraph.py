from graphviz import Graph

g = Graph('G', filename='g_c_n.gv', engine='dot')
g.attr(size='8,8')
g.attr(bgcolor='red:pink', label='Link Traceability', fontcolor='white')
countries = ['USA', 'China', 'Germany']
videos = ['Wild', 'Serious', 'World', 'Weather']
home_links = ['US', 'World', 'Politics', 'Business', 'Opinion', 'Health', 'Video']
states = ['AL', 'AR', 'CA', 'CO', 'DE', 'FL', 'GA', 'HI', 'KS', 'KY', 'LA']

with g.subgraph(name='cluster1') as c:
    c.attr(fillcolor='white', fontcolor='black', style='filled', gradientangle='270')
    c.attr('node', shape='tab', fillcolor='green:white', style='filled', gradientangle='100')

    c.node('cnn.com')
    c.node('Home')
    c.node('Video')
    c.node('News')


    for country in countries:
        c.node(country)
        c.edge('News', country)

    for link in home_links:
        c.node(link)
        c.edge('Home', link)

    for video in videos:
        c.node(video)
        c.edge('Video', video)

    c.edge('cnn.com', 'Home')
    c.edge('Home', 'News')
    c.edge('Home', 'Video')


g.view()