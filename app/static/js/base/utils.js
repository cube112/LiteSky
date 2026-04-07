// 函数：移除.is-hidden类
export function showElement(element) {
    element.classList.remove('is-hidden');
}


// 函数：添加.is-hidden类
export function hideElement(element) {
    element.classList.add('is-hidden');
}


// 函数：反转.is-hidden类
export function toggleElement(element) {
    element.classList.toggle('is-hidden');
}


// 函数：重置表单
export function resetForm(form) {
    form.reset();
}

