from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from views.comment_requests import get_comments_of_user, get_comments_of_post, create_comment, update_comment, delete_comment
from views.post_requests import get_single_post, get_posts_by_user, get_all_posts, create_post, update_post, delete_post
from views.user_requests import get_all_users, get_single_user, update_user, delete_user, create_user, login_user, get_id_of_user
from views.tag_requests import get_single_tag, create_tag, delete_tag, get_all_tags
from views.subscriptions import create_subscription, update_subscription, delete_subscription, get_subscriptions_of_author
from views.post_tag_requests import get_poststags_by_postid, create_post_tag, delete_post_tag
from views.category_requests import get_all_categories, create_category

class HandleRequests(BaseHTTPRequestHandler):
    """Handles the requests to this server"""

    def parse_url(self):
        """Parse the url into the resource and id"""
        path_params = self.path.split('/')
        resource = path_params[1]
        if '?' in resource:
            param = resource.split('?')[1]
            resource = resource.split('?')[0]
            pair = param.split('=')
            key = pair[0]
            value = pair[1]
            return (resource, key, value)
        else:
            id = None
            try:
                id = int(path_params[2])
            except (IndexError, ValueError):
                pass
            return (resource, id)

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the OPTIONS headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_GET(self):
        """Handle Get requests to the server"""
        
        self._set_headers(200)
        response = {}
        
        if '?' not in self.path:
            
            ( resource, id ) = self.parse_url()

            if resource == "posts":
                if id is not None:
                    response = get_single_post(id)
                else:
                    response = get_all_posts()
            if resource == "users":
                if id is not None:
                    response = get_single_user(id)
                else:
                    response = get_all_users()
            if resource == "tags":
                if id is not None:
                    response = get_single_tag(id)
                    print()
                else:
                    response = get_all_tags()
            if resource == "subscriptions":
                if id is not None:
                    response = get_subscriptions_of_author(id)
            if resource == "categories":
                if id is not None:
                    pass
                else:
                    response = get_all_categories()
            
        else:         
            (resource, query, value) = self.parse_url()
            if resource == "comments" and query=="postId":
                response = get_comments_of_post(value)
            if resource == "comments" and query=="authorId":
                response = get_comments_of_user(value)
            if resource == "posts" and query=="user_id":
                response = get_posts_by_user(value)
            if resource == "post_tags" and query=="post_id":
                response = get_poststags_by_postid(value)
            if resource == "users" and query =="username":
                response = get_id_of_user(value)

        self.wfile.write(json.dumps(response).encode())
        
    def do_POST(self):
        """Make a post request to the server"""
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = json.loads(self.rfile.read(content_len))
        response = ''
        resource, _ = self.parse_url()

        if resource == 'login':
            response = login_user(post_body)
        if resource == 'register':
            response = create_user(post_body)
        if resource == 'comments':
            response = json.dumps(create_comment(post_body))
        if resource == 'subscriptions':
            response = json.dumps(create_subscription(post_body))
        if resource == "posts":
            response = json.dumps(create_post(post_body))
        if resource == "users":
            response = json.dumps(create_user(post_body))
        if resource == "tags":
            response = json.dumps(create_tag(post_body))
        if resource == "post_tags":
            response = json.dumps(create_post_tag(post_body))
        if resource == 'categories':
            response = json.dumps(create_category(post_body))

        self.wfile.write(response.encode())

    def do_PUT(self):
        """Handles PUT requests to the server"""
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)
        (resource, id) = self.parse_url()
        
        success = False
        
        if resource == "comments":
            success = update_comment(id, post_body)
        if resource == "posts":
            success = update_post(id, post_body)
        if resource == "users":
            success = update_user(id, post_body)
        if resource == "subscriptions":
            success = update_subscription(id, post_body)
            
        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)

        self.wfile.write("".encode())
        
        
    def do_DELETE(self):
        """Handle DELETE Requests"""
        self._set_headers(204)

        (resource, id) = self.parse_url()
        if resource == "comments":
            delete_comment(id)
        if resource == "posts":
            delete_post(id)
        if resource == "users":
            delete_user(id)
        if resource == "tags":
            delete_tag(id)
        if resource == "subscriptions":
            delete_subscription(id)

        if resource == "post_tags":
            delete_post_tag(id)


def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
