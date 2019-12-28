from typing import Optional, Dict

class ConvoKitIndex:
    def __init__(self, utterances_index: Optional[Dict[str, str]] = None,
                 users_index: Optional[Dict[str, str]] = None,
                 conversations_index: Optional[Dict[str, str]] = None,
                 overall_index: Optional[Dict[str, str]] = None, version: Optional[int] = 0):
        self.utterances_index = utterances_index if utterances_index is not None else {}
        self.users_index = users_index if users_index is not None else {}
        self.conversations_index = conversations_index if conversations_index is not None else {}
        self.overall_index = overall_index if overall_index is not None else {}
        self.version = version

    def update_index(self, index_type: str, key: str, class_type: str):
        assert type(key) == str
        assert 'class' in class_type or class_type == 'bin'

        indices = {'utterance': self.utterances_index,
                   'conversation': self.conversations_index,
                   'user': self.users_index,
                   'corpus': self.overall_index}

        indices[index_type][key] = class_type

    def update_from_dict(self, meta_index: Dict):
        self.conversations_index = meta_index["conversations-index"]
        self.utterances_index = meta_index["utterances-index"]
        self.users_index = meta_index["users-index"]
        self.overall_index = meta_index["overall-index"]
        self.version = meta_index["version"]

    def to_dict(self, increment_version=True):
        retval = dict()
        retval["utterances-index"] = self.utterances_index
        retval["users-index"] = self.users_index
        retval["conversations-index"] = self.conversations_index
        retval["overall-index"] = self.overall_index
        retval["version"] = self.version + int(increment_version)
        return retval

    # def __eq__(self, other):
    #     # always true if other object is a ConvoKitIndex
    #     return isinstance(other, ConvoKitIndex)