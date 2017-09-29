import comparator
import bookParser

# parse records from elibrary and google scholar
parser = bookParser.bookParser()
parser.elibrary()
# all names for this book
# parser.scholar('Устойчивость нелинейных систем с неединственным состоянием равновесия')
# parser.scholar('Stability of nonlinear systems with nonunique equilibrium position(Russian book)')
# parser.scholar('Ustojcivost\'nelinejnych sistem s needinstvennym sostojaniem ravnovesija')
# parser.scholar('Устойчивость систем с неединственным состоянием равновесия')

comparator = comparator.comparator()

# in scholar and not in elibrary
with open('result/sch-elib.txt', 'w', encoding="utf8") as result:
    for i in comparator.diff('input/sch.txt', 'input/elib.txt'):
        result.write(comparator.sch_map.get(i))

# in elibrary and not in scholar
with open('result/elib-sch.txt', 'w', encoding="utf8") as result:
    for i in comparator.diff('input/elib.txt', 'input/sch.txt'):
        result.write(i)

comparator.sortRes("result/elib-sch.txt")
comparator.sortRes("result/sch-elib.txt")
