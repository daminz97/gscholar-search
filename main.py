from scholarly import scholarly
import argparse
import json

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="auto update of gscholar")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("--name", default=None, type=str, help="author name")
    group.add_argument("--id", default=None, type=str, help="author gscholar id")
    group.add_argument("--title", default=None, type=str, help="publication title")

    parser.add_argument("--bib", default=None, type=bool, help="generate bibtex")
    parser.add_argument("--output", default=".", type=str, help="save to output path")

    args = parser.parse_args()

    author_name = args.name
    author_id = args.id
    pub_title = args.title
    bibtex = args.bib
    output_path = args.output + '/output.txt'

    if author_name:
        author = next(scholarly.search_author(author_name))
        rst = scholarly.fill(author, sections=['basics', 'publications'])
    elif author_id:
        author = scholarly.search_author_id(author_id)
        rst = scholarly.fill(author, sections=['basics', 'publications'])
    elif pub_title:
        pub = next(scholarly.search_pubs(pub_title))
        rst = pub
    
    if pub_title and bibtex:
        pub = next(scholarly.search_pubs(pub_title))
        rst = scholarly.bibtex(pub)
    
    with open(output_path, 'w') as f:
        json.dump(rst, f)
        print('Results saved')