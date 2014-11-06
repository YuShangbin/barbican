"""
Copyright 2014 Rackspace

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from functionaltests.api.v1.models.base_models import BaseModel


class OrderModel(BaseModel):

    def __init__(self, type=None, name=None, status=None, secret_ref=None,
                 updated=None, created=None, meta=None, order_ref=None,
                 error_status_code=None, error_reason=None):
        super(OrderModel, self).__init__()
        self.type = type
        self.name = name
        self.status = status
        self.secret_ref = secret_ref
        self.updated = updated
        self.created = created
        self.meta = meta
        self.order_ref = order_ref
        self.error_status_code = error_status_code
        self.error_reason = error_reason