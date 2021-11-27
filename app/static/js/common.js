window.onload = () => {
  // 문서가 로드되면 call
  const ele = document.getElementById("flashModal");
  if (ele) {
    var myModal = new bootstrap.Modal(ele, {});
    myModal.show();
  }
};
// const test = () => {
//   axios
//     .get(
//       "/api/books/search?q=%ED%8C%8C%EC%9D%B4%EC%8D%AC&per_page=3&sort=popularity&page=1"
//     )
//     .then((response) => {
//       const users = response.data;
//       console.log(`GET data`, users);
//     })
//     .catch((error) => console.error(error));
// };

const node = document.getElementById("search_input");
if (node) {
  const searchParams = new URLSearchParams(window.location.search);
  node.value = searchParams.get("q");
  node.addEventListener("keyup", function (e) {
    console.log(node.value);
    if (e.key === "Enter") {
      // 1페이지 부터 보라고. page 매개변수를 지워준다.
      searchParams.delete("page");
      searchParams.set("q", node.value);
      window.location.replace(`/?${searchParams.toString()}`);
    }
  });
}

const returnBookClickHandler = (e) => {
  const target = e.target;
  const bookId = target.getAttribute("data-book-id");
  const postParams = {
    book_id: bookId,
    act: "write",
  };
  sendPost(`/book/${bookId}/return`, postParams);
};

const deleteBookClickHandler = (e) => {
  const target = e.target;
  const bookId = target.getAttribute("data-book-id");
  const reviewId = target.getAttribute("data-review-id");
  console.log(bookId);
  const postParams = {
    review_id: reviewId,
    act: "delete",
  };
  sendPost(`/book/${bookId}/review`, postParams);
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
