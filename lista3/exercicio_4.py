from collections import deque

class Action:
    def __init__(self, do_callable, undo_callable, description=""):
        self.do = do_callable
        self.undo = undo_callable
        self.description = description

class UndoStack:
    def __init__(self, max_history=None):
        self._undo = deque()  
        self._redo = deque() 

    def push(self, action: Action):
        action.do()
        self._undo.append(action)
        self._redo.clear()
       
        if self.max_history is not None:
            while len(self._undo) > self.max_history:
                self._undo.popleft()

    def undo(self):
        if not self._undo:
            print("Nada para desfazer.")
            return
        action = self._undo.pop()
        action.undo()
        self._redo.append(action)
        print(f"Desfeito: {action.description}")

    def redo(self):
        if not self._redo:
            print("Nada para refazer.")
            return
        action = self._redo.pop()
        action.do()
        self._undo.append(action)
        print(f"Refeito: {action.description}")

    def show_history(self):
        print("--- Histórico (undo lado direito) ---")
        for a in self._undo:
            print(a.description)
        print("--- fim histórico ---")
        print(f"undo_count={len(self._undo)} redo_count={len(self._redo)}\n")

buffer = {"text": ""}

def make_insert_action(buffer, text_to_insert):
    def do():
        buffer["text"] += text_to_insert
    def undo():
        buffer["text"] = buffer["text"][:-len(text_to_insert)]
    return Action(do, undo, description=f"Inserir '{text_to_insert}'")

def make_delete_last_action(buffer, k):
    state = {"removed": ""}
    def do():
        state["removed"] = buffer["text"][-k:] if k <= len(buffer["text"]) else buffer["text"]
        buffer["text"] = buffer["text"][:-k]
    def undo():
        buffer["text"] += state["removed"]
    return Action(do, undo, description=f"Deletar últimos {k} chars")

# ---------- Demonstração ----------
stack = UndoStack(max_history=100)

print("Estado inicial:", repr(buffer["text"]))

# Inserir "Hello "
stack.push(make_insert_action(buffer, "Hello "))
print("Após inserir 'Hello ':", repr(buffer["text"]))

# Inserir "world"
stack.push(make_insert_action(buffer, "world"))
print("Após inserir 'world':", repr(buffer["text"]))

# Inserir "!"
stack.push(make_insert_action(buffer, "!"))
print("Após inserir '!':", repr(buffer["text"]))

# Deletar último char (o "!")
stack.push(make_delete_last_action(buffer, 1))
print("Após deletar 1 char:", repr(buffer["text"]))

# Mostrar histórico atual
stack.show_history()

# Undo duas vezes
stack.undo()
print("Buffer depois de 1 undo:", repr(buffer["text"]))
stack.undo()
print("Buffer depois de 2 undo:", repr(buffer["text"]))

# Redo uma vez
stack.redo()
print("Buffer depois de 1 redo:", repr(buffer["text"]))

# Nova ação (insere '!!!') — isso limpa a pilha redo
stack.push(make_insert_action(buffer, "!!!"))
print("Após inserir '!!!':", repr(buffer["text"]))

# tentar redo (não tem, foi limpo)
stack.redo()

# Histórico final
stack.show_history()
print("Estado final do buffer:", repr(buffer["text"]))
