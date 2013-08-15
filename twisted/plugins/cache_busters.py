"""
Copyright 2013 Rackspace

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

from twisted.application.service import ServiceMaker


CacheBusters = ServiceMaker(
    ("An automatic cache invalidator which listens to a database replication "
     "protocol and then evicts keys from a cache."),
    "cache_busters",
    ("When there's something invalid, in your cache, who you gonna call, cache"
     "busters!"),
    "cache-busters",
)
