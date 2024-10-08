import os
from .annotation import create_annotation


def create_directories(base_dir, labels):
    for label in labels:
        dir_path = os.path.join(base_dir, label)
        os.makedirs(dir_path, exist_ok=True)


def save_annotation(directory, label, doc_id, annotation):
    file_path = os.path.join(directory, label, f"{doc_id}.tsv")

    with open(file_path, 'w', encoding='utf-8') as f:
        for sentence in annotation:
            for token, stem, lemma in sentence:
                f.write(f"{token}\t{stem}\t{lemma}\n")
            f.write("\n")


def process_and_save_annotations(dataset, split, label_map, output_dir):
    for i, example in enumerate(dataset[split]):
        text = example['text']
        label = label_map[example['label']]  # Преобразование метки в текстовый класс
        doc_id = f"{i:03d}"  # Используем номер записи как идентификатор
        annotation = create_annotation(text)
        save_annotation(output_dir, label, doc_id, annotation)

    print(f"Обработка и сохранение аннотаций для {split} завершена. Аннотации сохранены в {output_dir}.")

