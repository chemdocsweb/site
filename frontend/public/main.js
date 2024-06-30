function review_click() {
  var tb_review = this.querySelector('.review');
  if (tb_review.style.display === 'block') {
    tb_review.style.display = 'none';
  } else {
    reviews.forEach(review => review.style.display = 'none');
    tb_review.style.display = 'block';
  }
  var star = this.querySelector('.star');
  var star_rate = star.dataset.ratingVal;
  var star_width = (star_rate * 20) + '%';
  star.style.setProperty('--rating_width', star_width);
}

function subject_pagination() {
  var index = this.id - 1;
  subjects.forEach(subject => {
    subject.style.display = 'none';
  });
  sub_btns.forEach(btn => {
    btn.classList.remove('active');
  });
  subjects[index].style.display = 'block';
  sub_btns[index].classList.add('active');
  window.scrollTo(0, 0);
}