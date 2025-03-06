document.getElementById('addTaskBtn').addEventListener('click', function() {
  const taskInput = document.getElementById('taskInput');
  const taskValue = taskInput.value.trim();

  if (taskValue !== "") {
    addTaskToList(taskValue);
    taskInput.value = ""; // Очищаем поле ввода после добавления задачи
  }
});

function addTaskToList(taskText) {
  const taskList = document.getElementById('taskList');

  // Создаем новый элемент списка
  const li = document.createElement('li');
  li.classList.add('task-item');
  li.innerHTML = `
    <span>${taskText}</span>
    <div>
      <button class="complete" onclick="toggleTaskCompletion(this)">Mark as Done</button>
      <button onclick="removeTask(this)">Delete</button>
    </div>
  `;

  taskList.appendChild(li);
}

function toggleTaskCompletion(button) {
  const taskItem = button.closest('.task-item');
  taskItem.classList.toggle('completed');
  button.innerText = taskItem.classList.contains('completed') ? "Undo" : "Mark as Done";
}

function removeTask(button) {
  const taskItem = button.closest('.task-item');
  taskItem.remove();
}
