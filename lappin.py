//lappin and leas algorithm in python?
def read_graph(lines):
    g = {}
    for line in lines:
        words = line.split()
        if words[1] == '.':
            words = words[:1]
        g[words[0]] = words[1:]
    return g

def dump_graph(g):
    out = []
    def dump(key):
        for k in g[key]:
            dump(k)
        if key not in out:
            out.append(key)
    for k in g:
        dump(k)
    return out

'''
&gt;&gt;&gt; data = """Civic        Honda Car
... Honda        Manufacturer
... VW           Manufacturer
... Manufacturer .
... Car          .
... Beetle       VW Car
... """
&gt;&gt;&gt; g = read_graph(data.splitlines())
&gt;&gt;&gt; g
{'VW': ['Manufacturer'], 'Civic': ['Honda', 'Car'], 'Car': [],
'Honda': ['Manufacturer'], 'Beetle': ['VW', 'Car'], 'Manufacturer': []}
&gt;&gt;&gt; dump_graph(g)
['Manufacturer', 'VW', 'Honda', 'Car', 'Civic', 'Beetle']
&gt;&gt;&gt;
'''

