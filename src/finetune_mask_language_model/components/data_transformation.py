from transformers import AutoModelForMaskedLM
from transformers import AutoTokenizer
from datasets import load_from_disk

from src.finetune_mask_language_model.entity import DataTransformationConfig
import os


class DataTransformation:


    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer)


    def tokenize_function(self, examples):
        result = self.tokenizer(examples["text"])
        if self.tokenizer.is_fast:
            result["word_ids"] = [result.word_ids(i) for i in range(len(result["input_ids"]))]
        return result

    
    def convert(self):
        imdb_dataset = load_from_disk(self.config.data_path)
        imdb_dataset_t =  imdb_dataset.map(
            self.tokenize_function, 
            batched=True, 
            remove_columns=["text", "label"]
        )

        imdb_dataset_t.save_to_disk(os.path.join(self.config.root_dir, 'imdb_new'))










