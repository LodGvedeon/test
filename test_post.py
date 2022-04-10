from main import Post
# Test comment
data_raw = {
    'userId': 1,
    'id': 10,
    'title': 'SOme test title',
    'body': 'Choto tam'
}
post_new = Post(**data_raw)
post_new.print_info()

