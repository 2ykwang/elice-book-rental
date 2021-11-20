window.onload = () => {
  // 문서가 로드되면 call
  const ele = document.getElementById("flashModal");
  if (ele) {
    var myModal = new bootstrap.Modal(ele, {});
    myModal.show();
  }
};

const returnBookClickHandler = (e) => {
  const target = e.target;
  const bookId = target.getAttribute("data-book-id");
  const postParams = {
    book_id: bookId,
  };
  sendPost(`/book/${bookId}/return`, postParams);
  console.log(bookId);
};

const sendPost = (action, params) => {
  const form = document.createElement("form");

  form.setAttribute("method", "post");
  form.setAttribute("action", action);

  for (const key in params) {
    const field = document.createElement("input");
    field.setAttribute("type", "hidden");
    field.setAttribute("name", key);
    field.setAttribute("value", params[key]);
    form.appendChild(field);
  }
  document.body.appendChild(form);
  form.submit();
};
