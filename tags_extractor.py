import argparse
from file_tags_extractor import FileTagsExtractor
from dir_tags_extractor import DirTagsExtractor
from metadata_separator import ByKnownItemsSeparator
import itertools

def combinations_extractor(list):
    all_combinations = []
    for combination_size in range(0, len(list) + 1):
        combinations = itertools.combinations(list, combination_size)
        all_combinations.extend(combinations)
    return all_combinations


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('dir_path', type=str, help="Path to the repo directory.")
    args = parser.parse_args()
    known_operating_systems = { 'windows', 'solaris', 'linux', 'darwin', 'freebsd', 'netbsd', 'aix', 'dragonfly', 'openbsd', 'illumos', 'android', 'ios'}
    known_architecture = { 'amd64'}

    file_tags_extractor = FileTagsExtractor()
    dir_tags_extractor = DirTagsExtractor(file_tags_extractor)
    os_separator = ByKnownItemsSeparator(known_operating_systems)
    arch_separator = ByKnownItemsSeparator(known_architecture)
    tags = dir_tags_extractor.extract(args.dir_path)
    operating_systems, other = os_separator.extract(tags)
    architectures,other = arch_separator.extract(other)
    all_other_combinations = combinations_extractor(other)
    print(all_other_combinations)
    operating_systems.extend([''])
    architectures.extend([''])

    all_possible_combination = []
    for operating_system in operating_systems:
        for arch in architectures:
            for combination in all_other_combinations:
                # all_possible_combination.extend([(operating_system, arch)+combination])
                new_combination = (operating_system, arch)+combination
                print([new_combination[i] for i in range(len(new_combination))])



if __name__ == "__main__":
    main()