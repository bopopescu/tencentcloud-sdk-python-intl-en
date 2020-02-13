# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from tencentcloud.common.abstract_model import AbstractModel


class AddCdnDomainRequest(AbstractModel):
    """AddCdnDomain request structure.

    """

    def __init__(self):
        """
        :param Domain: Domain name
        :type Domain: str
        :param ServiceType: Business type of acceleration domain name
web: static acceleration
download: download acceleration
media: streaming media VOD acceleration
        :type ServiceType: str
        :param Origin: Origin server configuration
        :type Origin: :class:`tencentcloud.cdn.v20180606.models.Origin`
        :param ProjectId: Project ID, which is 0 by default, indicating **Default Project**
        :type ProjectId: int
        :param IpFilter: IP blacklist/whitelist configuration
        :type IpFilter: :class:`tencentcloud.cdn.v20180606.models.IpFilter`
        :param IpFreqLimit: IP access limit configuration
        :type IpFreqLimit: :class:`tencentcloud.cdn.v20180606.models.IpFreqLimit`
        :param StatusCodeCache: Status code cache configuration
        :type StatusCodeCache: :class:`tencentcloud.cdn.v20180606.models.StatusCodeCache`
        :param Compression: Smart compression configuration
        :type Compression: :class:`tencentcloud.cdn.v20180606.models.Compression`
        :param BandwidthAlert: Bandwidth cap configuration
        :type BandwidthAlert: :class:`tencentcloud.cdn.v20180606.models.BandwidthAlert`
        :param RangeOriginPull: Range origin-pull configuration
        :type RangeOriginPull: :class:`tencentcloud.cdn.v20180606.models.RangeOriginPull`
        :param FollowRedirect: 301/302 origin-pull follow-redirect configuration
        :type FollowRedirect: :class:`tencentcloud.cdn.v20180606.models.FollowRedirect`
        :param ErrorPage: Error code redirect configuration (This feature is in beta test and not fully available yet.)
        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ErrorPage`
        :param RequestHeader: Request header configuration
        :type RequestHeader: :class:`tencentcloud.cdn.v20180606.models.RequestHeader`
        :param ResponseHeader: Response header configuration
        :type ResponseHeader: :class:`tencentcloud.cdn.v20180606.models.ResponseHeader`
        :param DownstreamCapping: Download speed configuration
        :type DownstreamCapping: :class:`tencentcloud.cdn.v20180606.models.DownstreamCapping`
        :param CacheKey: Node cache key configuration
        :type CacheKey: :class:`tencentcloud.cdn.v20180606.models.CacheKey`
        :param ResponseHeaderCache: Header cache configuration
        :type ResponseHeaderCache: :class:`tencentcloud.cdn.v20180606.models.ResponseHeaderCache`
        :param VideoSeek: Video dragging configuration
        :type VideoSeek: :class:`tencentcloud.cdn.v20180606.models.VideoSeek`
        :param Cache: Cache expiration time configuration
        :type Cache: :class:`tencentcloud.cdn.v20180606.models.Cache`
        :param OriginPullOptimization: Cross-border linkage optimization configuration
        :type OriginPullOptimization: :class:`tencentcloud.cdn.v20180606.models.OriginPullOptimization`
        :param Https: Https acceleration configuration
        :type Https: :class:`tencentcloud.cdn.v20180606.models.Https`
        :param Authentication: Timestamp hotlink protection configuration
        :type Authentication: :class:`tencentcloud.cdn.v20180606.models.Authentication`
        :param Seo: SEO configuration
        :type Seo: :class:`tencentcloud.cdn.v20180606.models.Seo`
        :param ForceRedirect: Access protocol forced redirect configuration
        :type ForceRedirect: :class:`tencentcloud.cdn.v20180606.models.ForceRedirect`
        :param Referer: Referer hotlink protection configuration
        :type Referer: :class:`tencentcloud.cdn.v20180606.models.Referer`
        :param MaxAge: Browser cache configuration (This feature is in beta test and not fully available yet.)
        :type MaxAge: :class:`tencentcloud.cdn.v20180606.models.MaxAge`
        :param Ipv6: Ipv6 configuration (This feature is in beta test and not fully available yet.)
        :type Ipv6: :class:`tencentcloud.cdn.v20180606.models.Ipv6`
        :param SpecificConfig: Specific configuration for region attributes
Applicable to use cases where the configuration of accelerating domain names inside mainland China is inconsistent with the configuration outside mainland China.
        :type SpecificConfig: :class:`tencentcloud.cdn.v20180606.models.SpecificConfig`
        :param Area: Domain name acceleration region
mainland: acceleration inside mainland China
overseas: acceleration outside mainland China
global: global acceleration
To use overseas acceleration and global acceleration, you need to enable the overseas acceleration service first
        :type Area: str
        """
        self.Domain = None
        self.ServiceType = None
        self.Origin = None
        self.ProjectId = None
        self.IpFilter = None
        self.IpFreqLimit = None
        self.StatusCodeCache = None
        self.Compression = None
        self.BandwidthAlert = None
        self.RangeOriginPull = None
        self.FollowRedirect = None
        self.ErrorPage = None
        self.RequestHeader = None
        self.ResponseHeader = None
        self.DownstreamCapping = None
        self.CacheKey = None
        self.ResponseHeaderCache = None
        self.VideoSeek = None
        self.Cache = None
        self.OriginPullOptimization = None
        self.Https = None
        self.Authentication = None
        self.Seo = None
        self.ForceRedirect = None
        self.Referer = None
        self.MaxAge = None
        self.Ipv6 = None
        self.SpecificConfig = None
        self.Area = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.ServiceType = params.get("ServiceType")
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        self.ProjectId = params.get("ProjectId")
        if params.get("IpFilter") is not None:
            self.IpFilter = IpFilter()
            self.IpFilter._deserialize(params.get("IpFilter"))
        if params.get("IpFreqLimit") is not None:
            self.IpFreqLimit = IpFreqLimit()
            self.IpFreqLimit._deserialize(params.get("IpFreqLimit"))
        if params.get("StatusCodeCache") is not None:
            self.StatusCodeCache = StatusCodeCache()
            self.StatusCodeCache._deserialize(params.get("StatusCodeCache"))
        if params.get("Compression") is not None:
            self.Compression = Compression()
            self.Compression._deserialize(params.get("Compression"))
        if params.get("BandwidthAlert") is not None:
            self.BandwidthAlert = BandwidthAlert()
            self.BandwidthAlert._deserialize(params.get("BandwidthAlert"))
        if params.get("RangeOriginPull") is not None:
            self.RangeOriginPull = RangeOriginPull()
            self.RangeOriginPull._deserialize(params.get("RangeOriginPull"))
        if params.get("FollowRedirect") is not None:
            self.FollowRedirect = FollowRedirect()
            self.FollowRedirect._deserialize(params.get("FollowRedirect"))
        if params.get("ErrorPage") is not None:
            self.ErrorPage = ErrorPage()
            self.ErrorPage._deserialize(params.get("ErrorPage"))
        if params.get("RequestHeader") is not None:
            self.RequestHeader = RequestHeader()
            self.RequestHeader._deserialize(params.get("RequestHeader"))
        if params.get("ResponseHeader") is not None:
            self.ResponseHeader = ResponseHeader()
            self.ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("DownstreamCapping") is not None:
            self.DownstreamCapping = DownstreamCapping()
            self.DownstreamCapping._deserialize(params.get("DownstreamCapping"))
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("ResponseHeaderCache") is not None:
            self.ResponseHeaderCache = ResponseHeaderCache()
            self.ResponseHeaderCache._deserialize(params.get("ResponseHeaderCache"))
        if params.get("VideoSeek") is not None:
            self.VideoSeek = VideoSeek()
            self.VideoSeek._deserialize(params.get("VideoSeek"))
        if params.get("Cache") is not None:
            self.Cache = Cache()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("OriginPullOptimization") is not None:
            self.OriginPullOptimization = OriginPullOptimization()
            self.OriginPullOptimization._deserialize(params.get("OriginPullOptimization"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        if params.get("Authentication") is not None:
            self.Authentication = Authentication()
            self.Authentication._deserialize(params.get("Authentication"))
        if params.get("Seo") is not None:
            self.Seo = Seo()
            self.Seo._deserialize(params.get("Seo"))
        if params.get("ForceRedirect") is not None:
            self.ForceRedirect = ForceRedirect()
            self.ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Referer") is not None:
            self.Referer = Referer()
            self.Referer._deserialize(params.get("Referer"))
        if params.get("MaxAge") is not None:
            self.MaxAge = MaxAge()
            self.MaxAge._deserialize(params.get("MaxAge"))
        if params.get("Ipv6") is not None:
            self.Ipv6 = Ipv6()
            self.Ipv6._deserialize(params.get("Ipv6"))
        if params.get("SpecificConfig") is not None:
            self.SpecificConfig = SpecificConfig()
            self.SpecificConfig._deserialize(params.get("SpecificConfig"))
        self.Area = params.get("Area")


class AddCdnDomainResponse(AbstractModel):
    """AddCdnDomain response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AdvanceCacheRule(AbstractModel):
    """Rules of cache configuration advanced version

    """

    def __init__(self):
        """
        :param CacheType: Rule types:
all: all files take effect
file: specified file suffixes take effect
directory: specified paths take effect
path: specified absolute paths take effect
default: the cache rules when the origin server has not returned max-age
Note: this field may return null, indicating that no valid values can be obtained.
        :type CacheType: str
        :param CacheContents: Matching content under the corresponding types:
For "all", enter an asterisk (*).
For "file", enter the suffix, such as jpg, txt.
For "directory", enter the path, such as /xxx/test/.
For "path", enter the corresponding absolute path, such as /xxx/test.html.
For "default", enter "no max-age".
Note: this field may return null, indicating that no valid values can be obtained.
        :type CacheContents: list of str
        :param CacheTime: Cache expiration time
Unit: second. The maximum value is 365 days.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CacheTime: int
        """
        self.CacheType = None
        self.CacheContents = None
        self.CacheTime = None


    def _deserialize(self, params):
        self.CacheType = params.get("CacheType")
        self.CacheContents = params.get("CacheContents")
        self.CacheTime = params.get("CacheTime")


class AdvancedCache(AbstractModel):
    """Cache expiration configuration advanced version (This feature is in beta test and not fully available yet.)
    Note: this version does not support setting the home page cache rule.

    """

    def __init__(self):
        """
        :param CacheRules: Cache expiration rule
Note: this field may return null, indicating that no valid values can be obtained.
        :type CacheRules: list of AdvanceCacheRule
        :param IgnoreCacheControl: Forced cache configuration
on: enabled
off: disabled
When it is enabled, if the origin server returns no-cache, no-store headers, node caching will still be performed according to the cache expiration rules.
It is disabled by default
Note: this field may return null, indicating that no valid values can be obtained.
        :type IgnoreCacheControl: str
        :param IgnoreSetCookie: Ignore the Set-Cookie header of an origin server
on: enabled
off: disabled
It is disabled by default
Note: this field may return null, indicating that no valid values can be obtained.
        :type IgnoreSetCookie: str
        """
        self.CacheRules = None
        self.IgnoreCacheControl = None
        self.IgnoreSetCookie = None


    def _deserialize(self, params):
        if params.get("CacheRules") is not None:
            self.CacheRules = []
            for item in params.get("CacheRules"):
                obj = AdvanceCacheRule()
                obj._deserialize(item)
                self.CacheRules.append(obj)
        self.IgnoreCacheControl = params.get("IgnoreCacheControl")
        self.IgnoreSetCookie = params.get("IgnoreSetCookie")


class Authentication(AbstractModel):
    """Timestamp hotlink protection configuration

    """

    def __init__(self):
        """
        :param Switch: Hotlink protection configuration switch
on: enabled
off: disabled
When it is enabled, only one mode needs to be configured. Other modes need to be set to null.
        :type Switch: str
        :param TypeA: Timestamp hotlink protection mode A configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type TypeA: :class:`tencentcloud.cdn.v20180606.models.AuthenticationTypeA`
        :param TypeB: Timestamp hotlink protection mode B configuration (the mode B backend is being upgraded and the configuration is currently not supported)
Note: this field may return null, indicating that no valid values can be obtained.
        :type TypeB: :class:`tencentcloud.cdn.v20180606.models.AuthenticationTypeB`
        :param TypeC: Timestamp hotlink protection mode C configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type TypeC: :class:`tencentcloud.cdn.v20180606.models.AuthenticationTypeC`
        :param TypeD: Timestamp hotlink protection mode D configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type TypeD: :class:`tencentcloud.cdn.v20180606.models.AuthenticationTypeD`
        """
        self.Switch = None
        self.TypeA = None
        self.TypeB = None
        self.TypeC = None
        self.TypeD = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("TypeA") is not None:
            self.TypeA = AuthenticationTypeA()
            self.TypeA._deserialize(params.get("TypeA"))
        if params.get("TypeB") is not None:
            self.TypeB = AuthenticationTypeB()
            self.TypeB._deserialize(params.get("TypeB"))
        if params.get("TypeC") is not None:
            self.TypeC = AuthenticationTypeC()
            self.TypeC._deserialize(params.get("TypeC"))
        if params.get("TypeD") is not None:
            self.TypeD = AuthenticationTypeD()
            self.TypeD._deserialize(params.get("TypeD"))


class AuthenticationTypeA(AbstractModel):
    """Timestamp hotlink protection mode A configuration
    The access URL format of timestamp hotlink protection mode A is as follows: http://DomainName/Filename?sign=timestamp-rand-uid-md5hash
    Here, timestamp is a decimal timestamp in Unix format;
    rand is a random string composed of 0-100 characters, including digits, upper and lower-case letters.
    uid is 0;
    md5hash: MD5 (file path-timestamp-rand-uid-custom key)

    """

    def __init__(self):
        """
        :param SecretKey: The key for signature calculation
Only digits, upper and lower-case letters are allowed. Length limit: 6-32 characters.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SecretKey: str
        :param SignParam: Signature parameter name configuration
Only upper and lower-case letters, digits, and underscores (_) are allowed. It cannot start with a digit. Length limit: 1-100 characters.
        :type SignParam: str
        :param ExpireTime: Signature expiration time settings
Unit: second. The maximum value is 31536000.
        :type ExpireTime: int
        :param FileExtensions: File extension list settings for authentication/no authentication
If it contains an asterisk (*), this indicates all files.
        :type FileExtensions: list of str
        :param FilterType: whitelist: indicating that all types apart from the FileExtensions list are authenticated
blacklist: indicating that only the types in the FileExtensions list are authenticated
        :type FilterType: str
        """
        self.SecretKey = None
        self.SignParam = None
        self.ExpireTime = None
        self.FileExtensions = None
        self.FilterType = None


    def _deserialize(self, params):
        self.SecretKey = params.get("SecretKey")
        self.SignParam = params.get("SignParam")
        self.ExpireTime = params.get("ExpireTime")
        self.FileExtensions = params.get("FileExtensions")
        self.FilterType = params.get("FilterType")


class AuthenticationTypeB(AbstractModel):
    """Timestamp hotlink protection mode B configuration (the mode B is under the platform upgrading and the configuration is currently not supported)

    """

    def __init__(self):
        """
        :param SecretKey: The key for signature calculation
Only digits, upper and lower-case letters are allowed. Length limit: 6-32 characters.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SecretKey: str
        :param ExpireTime: Signature expiration time settings
Unit: second. The maximum value is 31536000.
        :type ExpireTime: int
        :param FileExtensions: File extension list settings for authentication/no authentication
If it contains an asterisk (*), this indicates all files.
        :type FileExtensions: list of str
        :param FilterType: whitelist: indicating that all types apart from the FileExtensions list are authenticated
blacklist: indicating that only the types in the FileExtensions list are authenticated
        :type FilterType: str
        """
        self.SecretKey = None
        self.ExpireTime = None
        self.FileExtensions = None
        self.FilterType = None


    def _deserialize(self, params):
        self.SecretKey = params.get("SecretKey")
        self.ExpireTime = params.get("ExpireTime")
        self.FileExtensions = params.get("FileExtensions")
        self.FilterType = params.get("FilterType")


class AuthenticationTypeC(AbstractModel):
    """Timestamp hotlink protection mode C configuration
    The access URL format of timestamp hotlink protection mode C is as follows: http://DomainName/md5hash/timestamp/FileName
    Here, timestamp is a hexadecimal timestamp in Unix format;
    md5hash: MD5 (custom key + file path + timestamp)

    """

    def __init__(self):
        """
        :param SecretKey: The key for signature calculation
Only digits, upper and lower-case letters are allowed. Length limit: 6-32 characters.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SecretKey: str
        :param ExpireTime: Signature expiration time settings
Unit: second. The maximum value is 31536000.
        :type ExpireTime: int
        :param FileExtensions: File extension list settings for authentication/no authentication
If it contains an asterisk (*), this indicates all files.
        :type FileExtensions: list of str
        :param FilterType: whitelist: indicating that all types apart from the FileExtensions list are authenticated
blacklist: indicating that only the types in the FileExtensions list are authenticated
        :type FilterType: str
        """
        self.SecretKey = None
        self.ExpireTime = None
        self.FileExtensions = None
        self.FilterType = None


    def _deserialize(self, params):
        self.SecretKey = params.get("SecretKey")
        self.ExpireTime = params.get("ExpireTime")
        self.FileExtensions = params.get("FileExtensions")
        self.FilterType = params.get("FilterType")


class AuthenticationTypeD(AbstractModel):
    """Timestamp hotlink protection mode D configuration
    The access URL format of timestamp hotlink protection mode D is as follows: http://DomainName/FileName?sign=md5hash&t=timestamp
    Here, timestamp is a decimal or hexadecimal timestamp in Unix format;
    md5hash: MD5 (custom key + file path + timestamp)

    """

    def __init__(self):
        """
        :param SecretKey: The key for signature calculation
Only digits, upper and lower-case letters are allowed. Length limit: 6-32 characters.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SecretKey: str
        :param ExpireTime: Signature expiration time settings
Unit: second. The maximum value is 31536000.
        :type ExpireTime: int
        :param FileExtensions: File extension list settings for authentication/no authentication
If it contains an asterisk (*), this indicates all files.
        :type FileExtensions: list of str
        :param FilterType: whitelist: indicating that all types apart from the FileExtensions list are authenticated
blacklist: indicating that only the types in the FileExtensions list are authenticated
        :type FilterType: str
        :param SignParam: Signature parameter name configuration
Only upper and lower-case letters, digits, and underscores (_) are allowed. It cannot start with a digit. Length limit: 1-100 characters.
        :type SignParam: str
        :param TimeParam: Timestamp parameter name settings
Only upper and lower-case letters, digits, and underscores (_) are allowed. It cannot start with a digit. Length limit: 1-100 characters.
        :type TimeParam: str
        :param TimeFormat: Timestamp settings
dec: decimal
hex: hexadecimal
        :type TimeFormat: str
        """
        self.SecretKey = None
        self.ExpireTime = None
        self.FileExtensions = None
        self.FilterType = None
        self.SignParam = None
        self.TimeParam = None
        self.TimeFormat = None


    def _deserialize(self, params):
        self.SecretKey = params.get("SecretKey")
        self.ExpireTime = params.get("ExpireTime")
        self.FileExtensions = params.get("FileExtensions")
        self.FilterType = params.get("FilterType")
        self.SignParam = params.get("SignParam")
        self.TimeParam = params.get("TimeParam")
        self.TimeFormat = params.get("TimeFormat")


class BandwidthAlert(AbstractModel):
    """Bandwidth cap configuration. It is disabled by default.

    """

    def __init__(self):
        """
        :param Switch: Bandwidth cap configuration switch
on: enabled
off: disabled
        :type Switch: str
        :param BpsThreshold: Bandwidth cap threshold (in bps)
Note: this field may return null, indicating that no valid values can be obtained.
        :type BpsThreshold: int
        :param CounterMeasure: Operation after threshold is reached
RESOLVE_DNS_TO_ORIGIN: directly origin-pull. It is only supported for domain names of external origin.
RETURN_404: return 404 to all requests.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CounterMeasure: str
        :param LastTriggerTime: The last time the bandwidth cap threshold was triggered
Note: this field may return null, indicating that no valid values can be obtained.
        :type LastTriggerTime: str
        """
        self.Switch = None
        self.BpsThreshold = None
        self.CounterMeasure = None
        self.LastTriggerTime = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BpsThreshold = params.get("BpsThreshold")
        self.CounterMeasure = params.get("CounterMeasure")
        self.LastTriggerTime = params.get("LastTriggerTime")


class BriefDomain(AbstractModel):
    """The concise CDN domain name information

    """

    def __init__(self):
        """
        :param ResourceId: Domain name ID.
        :type ResourceId: str
        :param AppId: Tencent Cloud account ID.
        :type AppId: int
        :param Domain: CDN acceleration domain name.
        :type Domain: str
        :param Cname: Domain name CNAME.
        :type Cname: str
        :param Status: Domain name status. pending: under review; rejected: review failed; processing: review succeeded and under deployment; online: enabled; offline: disabled; deleted: deleted.
        :type Status: str
        :param ProjectId: Project ID.
        :type ProjectId: int
        :param ServiceType: Domain name business type. web: static acceleration; download: download acceleration; media: streaming media acceleration.
        :type ServiceType: str
        :param CreateTime: Domain name creation time.
        :type CreateTime: str
        :param UpdateTime: Domain name update time.
        :type UpdateTime: str
        :param Origin: Origin server configuration details.
        :type Origin: :class:`tencentcloud.cdn.v20180606.models.Origin`
        :param Disable: Domain name block status, including normal, overdue, quota, malicious, ddos, idle, unlicensed, capping, and readonly.
        :type Disable: str
        :param Area: Acceleration region, including mainland, overseas, and global.
        :type Area: str
        :param Readonly: Domain name lock status. normal: not locked; mainland: locked in mainland China; overseas: locked outside mainland China; global: locked globally.
        :type Readonly: str
        """
        self.ResourceId = None
        self.AppId = None
        self.Domain = None
        self.Cname = None
        self.Status = None
        self.ProjectId = None
        self.ServiceType = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Origin = None
        self.Disable = None
        self.Area = None
        self.Readonly = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.AppId = params.get("AppId")
        self.Domain = params.get("Domain")
        self.Cname = params.get("Cname")
        self.Status = params.get("Status")
        self.ProjectId = params.get("ProjectId")
        self.ServiceType = params.get("ServiceType")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        self.Disable = params.get("Disable")
        self.Area = params.get("Area")
        self.Readonly = params.get("Readonly")


class Cache(AbstractModel):
    """Node cache expiration time configuration, including the following two types:
    + Basic cache expiration rules configuration
    + Advanced cache expiration rules configuration

    """

    def __init__(self):
        """
        :param SimpleCache: Basic cache expiration time configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type SimpleCache: :class:`tencentcloud.cdn.v20180606.models.SimpleCache`
        :param AdvancedCache: Advanced cache expiration time configuration (This feature is in beta test and not fully available yet.)
Note: this field may return null, indicating that no valid values can be obtained.
        :type AdvancedCache: :class:`tencentcloud.cdn.v20180606.models.AdvancedCache`
        """
        self.SimpleCache = None
        self.AdvancedCache = None


    def _deserialize(self, params):
        if params.get("SimpleCache") is not None:
            self.SimpleCache = SimpleCache()
            self.SimpleCache._deserialize(params.get("SimpleCache"))
        if params.get("AdvancedCache") is not None:
            self.AdvancedCache = AdvancedCache()
            self.AdvancedCache._deserialize(params.get("AdvancedCache"))


class CacheKey(AbstractModel):
    """Cache key configuration (filter parameter configuration)

    """

    def __init__(self):
        """
        :param FullUrlCache: Whether to enable full-path cache
on: enable full-path cache (i.e., disable parameter filter)
off: disable full-path cache (i.e., enable parameter filter)
        :type FullUrlCache: str
        """
        self.FullUrlCache = None


    def _deserialize(self, params):
        self.FullUrlCache = params.get("FullUrlCache")


class CacheOptResult(AbstractModel):
    """Result of blocking/unblocking URLs

    """

    def __init__(self):
        """
        :param SuccessUrls: List of succeeded URLs
Note: This field may return null, indicating that no valid values can be obtained.
        :type SuccessUrls: list of str
        :param FailUrls: List of failed URLs
Note: This field may return null, indicating that no valid values can be obtained.
        :type FailUrls: list of str
        """
        self.SuccessUrls = None
        self.FailUrls = None


    def _deserialize(self, params):
        self.SuccessUrls = params.get("SuccessUrls")
        self.FailUrls = params.get("FailUrls")


class CappingRule(AbstractModel):
    """Downstream speed limit configuration rules. Up to 100 entries can be configured.

    """

    def __init__(self):
        """
        :param RuleType: Rule types:
all: all files take effect
file: specified file suffixes take effect
directory: specified paths take effect
path: specified absolute paths take effect
        :type RuleType: str
        :param RulePaths: Matching content under the corresponding types for RuleType: 
For "all", enter an asterisk (*).
For "file", enter the suffix, such as jpg, txt.
For "directory", enter the path, such as /xxx/test/.
For "path", enter the corresponding absolute path, such as /xxx/test.html.
        :type RulePaths: list of str
        :param KBpsThreshold: Downstream speed value settings (in KB/s)
        :type KBpsThreshold: int
        """
        self.RuleType = None
        self.RulePaths = None
        self.KBpsThreshold = None


    def _deserialize(self, params):
        self.RuleType = params.get("RuleType")
        self.RulePaths = params.get("RulePaths")
        self.KBpsThreshold = params.get("KBpsThreshold")


class CdnData(AbstractModel):
    """Detailed access data

    """

    def __init__(self):
        """
        :param Metric: Queries the specified metric:
flux: traffic (in bytes)
bandwidth: bandwidth (in bps)
request: number of requests
fluxHitRate: traffic hit rate (in %)
statusCode: status code. The aggregate data for 2xx, 3xx, 4xx, and 5xx status codes will be returned (in entries)
2XX: Returns the aggregate list of 2xx status codes and the data for status codes starting with 2 (in entries)
3XX: Returns the aggregate list of 3xx status codes and the data for status codes starting with 3 (in entries)
4XX: Returns the aggregate list of 4xx status codes and the data for status codes starting with 4 (in entries)
5XX: Returns the aggregate list of 5xx status codes and the data for status codes starting with 5 (in entries)
Alternatively, you can specify a status code for querying.
        :type Metric: str
        :param DetailData: Detailed data combination
        :type DetailData: list of TimestampData
        :param SummarizedData: Aggregate data combination
        :type SummarizedData: :class:`tencentcloud.cdn.v20180606.models.SummarizedData`
        """
        self.Metric = None
        self.DetailData = None
        self.SummarizedData = None


    def _deserialize(self, params):
        self.Metric = params.get("Metric")
        if params.get("DetailData") is not None:
            self.DetailData = []
            for item in params.get("DetailData"):
                obj = TimestampData()
                obj._deserialize(item)
                self.DetailData.append(obj)
        if params.get("SummarizedData") is not None:
            self.SummarizedData = SummarizedData()
            self.SummarizedData._deserialize(params.get("SummarizedData"))


class CdnIp(AbstractModel):
    """CdnIp attribute details

    """

    def __init__(self):
        """
        :param Ip: IP of the node.
        :type Ip: str
        :param Platform: Whether the IP is a Tencent Cloud CDN cache node. `yes`: it is a Tencent Cloud CDN cache node; `no`: it is not.
        :type Platform: str
        :param Location: District/country where the node is located. `unknown`: the node location is unknown.
        :type Location: str
        :param History: Activation and deactivation history of the node.
        :type History: list of CdnIpHistory
        :param Area: Service region of the node. `mainland`: Mainland China; `overseas`: outside Mainland China; `unknown`: unknown
        :type Area: str
        """
        self.Ip = None
        self.Platform = None
        self.Location = None
        self.History = None
        self.Area = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Platform = params.get("Platform")
        self.Location = params.get("Location")
        if params.get("History") is not None:
            self.History = []
            for item in params.get("History"):
                obj = CdnIpHistory()
                obj._deserialize(item)
                self.History.append(obj)
        self.Area = params.get("Area")


class CdnIpHistory(AbstractModel):
    """Activation and deactivation history of a CDN IP node.

    """

    def __init__(self):
        """
        :param Status: Node status. `online`: activated; `offline`: deactivated
        :type Status: str
        :param Datetime: Operation time. If its value is `null`, it means there is no status change record.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Datetime: str
        """
        self.Status = None
        self.Datetime = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Datetime = params.get("Datetime")


class ClientCert(AbstractModel):
    """HTTPS client certificate configuration

    """

    def __init__(self):
        """
        :param Certificate: Client Certificate
PEM format, requires Base64 encoding.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Certificate: str
        :param CertName: Client certificate name
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertName: str
        :param ExpireTime: Certificate expiration time
When it is used as an input parameter, it can be left blank.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param DeployTime: Certificate issuance time
When it is used as an input parameter, it can be left blank.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeployTime: str
        """
        self.Certificate = None
        self.CertName = None
        self.ExpireTime = None
        self.DeployTime = None


    def _deserialize(self, params):
        self.Certificate = params.get("Certificate")
        self.CertName = params.get("CertName")
        self.ExpireTime = params.get("ExpireTime")
        self.DeployTime = params.get("DeployTime")


class Compatibility(AbstractModel):
    """Whether it is compatible with configurations in old versions

    """

    def __init__(self):
        """
        :param Code: Compatibility flag status code.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Code: int
        """
        self.Code = None


    def _deserialize(self, params):
        self.Code = params.get("Code")


class Compression(AbstractModel):
    """Smart compression configuration. By default, Gzip compression is performed for files with js, html, css, xml, json, shtml, and htm suffixes, and with sizes between 256 and 2097152 bytes.

    """

    def __init__(self):
        """
        :param Switch: Smart compression configuration switch
on: enabled
off: disabled
        :type Switch: str
        :param CompressionRules: Compression rules array
Note: this field may return null, indicating that no valid values can be obtained.
        :type CompressionRules: list of CompressionRule
        """
        self.Switch = None
        self.CompressionRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("CompressionRules") is not None:
            self.CompressionRules = []
            for item in params.get("CompressionRules"):
                obj = CompressionRule()
                obj._deserialize(item)
                self.CompressionRules.append(obj)


class CompressionRule(AbstractModel):
    """Compression rules configuration. Up to 100 entries can be set.

    """

    def __init__(self):
        """
        :param Compress: true: must be set as true, to enable compression
Note: this field may return null, indicating that no valid values can be obtained.
        :type Compress: bool
        :param FileExtensions: Compress according to the file suffix type
Such as: jpg, txt
Note: this field may return null, indicating that no valid values can be obtained.
        :type FileExtensions: list of str
        :param MinLength: The minimum file size to trigger compression (in bytes)
Note: this field may return null, indicating that no valid values can be obtained.
        :type MinLength: int
        :param MaxLength: The maximum file size to trigger compression (in bytes)
The maximum value is 30 MB
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxLength: int
        :param Algorithms: File compression algorithm
gzip: specifies Gzip compression
brotli: It can be enabled when the Gzip compression is specified
Note: this field may return null, indicating that no valid values can be obtained.
        :type Algorithms: list of str
        """
        self.Compress = None
        self.FileExtensions = None
        self.MinLength = None
        self.MaxLength = None
        self.Algorithms = None


    def _deserialize(self, params):
        self.Compress = params.get("Compress")
        self.FileExtensions = params.get("FileExtensions")
        self.MinLength = params.get("MinLength")
        self.MaxLength = params.get("MaxLength")
        self.Algorithms = params.get("Algorithms")


class DeleteCdnDomainRequest(AbstractModel):
    """DeleteCdnDomain request structure.

    """

    def __init__(self):
        """
        :param Domain: Domain name
The domain name status should be **Disabled**
        :type Domain: str
        """
        self.Domain = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")


class DeleteCdnDomainResponse(AbstractModel):
    """DeleteCdnDomain response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeCdnDataRequest(AbstractModel):
    """DescribeCdnData request structure.

    """

    def __init__(self):
        """
        :param StartTime: Queries start time, such as 2018-09-04 10:40:00; the returned result is later than or equal to the specified time.
According to the specified time granularity, forward rounding is applied; for example, if the query end time is 2018-09-04 10:40:00 and the query time granularity is 1 hour, the time for the first returned entry will be 2018-09-04 10:00:00.
The gap between the start time and end time should be less than or equal to 90 days.
        :type StartTime: str
        :param EndTime: Queries end time, such as 2018-09-04 10:40:00; the returned result is earlier than or equal to the specified time.
According to the specified time granularity, forward rounding is applied; for example, if the query start time is 2018-09-04 10:40:00 and the query time granularity is 1 hour, the time for the last returned entry will be 2018-09-04 10:00:00.
The gap between the start time and end time should be less than or equal to 90 days.
        :type EndTime: str
        :param Metric: Specifies the query metric, which can be:
flux: traffic (in bytes)
bandwidth: bandwidth (in bps)
request: number of requests
fluxHitRate: traffic hit rate (in %)
statusCode: status code. The aggregate data for 2xx, 3xx, 4xx, and 5xx status codes will be returned (in entries)
2xx: Returns the aggregate list of 2xx status codes and the data for status codes starting with 2 (in entries)
3xx: Returns the aggregate list of 3xx status codes and the data for status codes starting with 3 (in entries)
4xx: Returns the aggregate list of 4xx status codes and the data for status codes starting with 4 (in entries)
5xx: Returns the aggregate list of 5xx status codes and the data for status codes starting with 5 (in entries)
It is supported to specify a status code for query. The return will be empty if the status code has never been generated.
        :type Metric: str
        :param Domains: Specifies the list of domain names to be queried
Up to 30 domain names can be queried at a time
        :type Domains: list of str
        :param Project: Specifies the project ID to be queried, which can be viewed [here](https://console.cloud.tencent.com/project)
Please note that if domain names are specified, this parameter will be ignored.
        :type Project: int
        :param Interval: Time granularity; valid values:
`min`: data with 1-minute granularity is returned when the queried period is no longer than 24 hours. This value is not supported if the service region you want to query is outside Mainland China;
`5min`: data with 5-minute granularity is returned when the queried period is no longer than 31 days;
`hour`: data with 1-hour granularity is returned when the queried period is no longer than 31 days;
`day`: data with 1-day granularity is returned when the queried period is longer than 31 days.
        :type Interval: str
        :param Detail: The aggregate data for multiple domain names is returned by default (false) during a multi-domain-name query.
You can set it to true to return the details for each Domain (the statusCode metric is currently not supported)
        :type Detail: bool
        :param Isp: Specifies an ISP when you query the CDN data within Mainland China. If it is left blank, all ISPs will be queried.
To view ISP codes, see [ISP Code Mappings](https://cloud.tencent.com/document/product/228/6316#.E5.8C.BA.E5.9F.9F-.2F-.E8.BF.90.E8.90.A5.E5.95.86.E6.98.A0.E5.B0.84.E8.A1.A8)
If you have specified an ISP, you cannot specify a province or an IP protocol for the same query.
        :type Isp: int
        :param District: Specifies a province when you query the CDN data within Mainland China. If it is left blank, all provinces will be queried.
Specifies a country/region when you query the CDN data outside Mainland China. If it is left blank, all countries/regions will be queried.
To view codes of provinces or countries/regions, see [Province Code Mappings](https://cloud.tencent.com/document/product/228/6316#.E5.8C.BA.E5.9F.9F-.2F-.E8.BF.90.E8.90.A5.E5.95.86.E6.98.A0.E5.B0.84.E8.A1.A8)
If you have specified a province for your query on CDN data within mainland China, you cannot specify an ISP or an IP protocol for the same query.
        :type District: int
        :param Protocol: Specifies the protocol to be queried; if you leave it blank, all protocols will be queried.
all: All protocols
http: specifies the HTTP metric to be queried
https: specifies the HTTPS metric to be queried
        :type Protocol: str
        :param DataSource: Specifies the data source to be queried, which can be seen as the whitelist function.
        :type DataSource: str
        :param IpProtocol: Specifies an IP protocol; if it is left blank, all IP protocols will be queried.
`all`: All protocols
`ipv4`: IPv4
`ipv6`: IPv6
If the IP protocol to be queried is specified, the district and ISP cannot be specified at the same time
        :type IpProtocol: str
        :param Area: Specifies a service region. If this value is left blank, CDN data within Mainland China will be queried.
`mainland`: specifies to query CDN data within Mainland China;
`overseas`: specifies to query CDN data outside Mainland China.
        :type Area: str
        :param AreaType: Specifies a region type for your query on CDN data outside Mainland China. If this parameter is left blank, data on the service region will be queried. This parameter is valid only when `Area` is `overseas`.
`server`: specifies to query data on the service region where Tencent Cloud CDN nodes are located;
`client`: specifies to query data on the client region where the request devices are located.
        :type AreaType: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Metric = None
        self.Domains = None
        self.Project = None
        self.Interval = None
        self.Detail = None
        self.Isp = None
        self.District = None
        self.Protocol = None
        self.DataSource = None
        self.IpProtocol = None
        self.Area = None
        self.AreaType = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Metric = params.get("Metric")
        self.Domains = params.get("Domains")
        self.Project = params.get("Project")
        self.Interval = params.get("Interval")
        self.Detail = params.get("Detail")
        self.Isp = params.get("Isp")
        self.District = params.get("District")
        self.Protocol = params.get("Protocol")
        self.DataSource = params.get("DataSource")
        self.IpProtocol = params.get("IpProtocol")
        self.Area = params.get("Area")
        self.AreaType = params.get("AreaType")


class DescribeCdnDataResponse(AbstractModel):
    """DescribeCdnData response structure.

    """

    def __init__(self):
        """
        :param Interval: Time granularity of the returned data. Specify one of the following during querying:
min: 1 minute
5min: 5 minutes
hour: 1 hour
day: 1 day
        :type Interval: str
        :param Data: Returned data details of the specified conditional query
        :type Data: list of ResourceData
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Interval = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Interval = params.get("Interval")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ResourceData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCdnDomainLogsRequest(AbstractModel):
    """DescribeCdnDomainLogs request structure.

    """

    def __init__(self):
        """
        :param Domain: Specifies a domain name for the query
        :type Domain: str
        :param StartTime: Starting time, such as `2019-09-04 00:00:00`
        :type StartTime: str
        :param EndTime: End time, such as `2019-09-04 12:00:00`
        :type EndTime: str
        :param Offset: Offset for paged queries. Default value: 0 (the first page)
        :type Offset: int
        :param Limit: Limit on paged queries. Default value: 100. Maximum value: 1,000
        :type Limit: int
        :param Area: Specifies a region for the query.
`mainland`: specifies to return the download link of logs on acceleration within Mainland China;
`overseas`: specifies to return the download link of logs on acceleration outside Mainland China;
`global`: specifies to return a download link of logs on acceleration within Mainland China and a link of logs on acceleration outside Mainland China.
Default value: `mainland`.
        :type Area: str
        """
        self.Domain = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None
        self.Area = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Area = params.get("Area")


class DescribeCdnDomainLogsResponse(AbstractModel):
    """DescribeCdnDomainLogs response structure.

    """

    def __init__(self):
        """
        :param DomainLogs: Download link of the log package
        :type DomainLogs: list of DomainLog
        :param TotalCount: Total number of entries obtained
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DomainLogs = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DomainLogs") is not None:
            self.DomainLogs = []
            for item in params.get("DomainLogs"):
                obj = DomainLog()
                obj._deserialize(item)
                self.DomainLogs.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeCdnIpRequest(AbstractModel):
    """DescribeCdnIp request structure.

    """

    def __init__(self):
        """
        :param Ips: List of IPs to be queried
        :type Ips: list of str
        """
        self.Ips = None


    def _deserialize(self, params):
        self.Ips = params.get("Ips")


class DescribeCdnIpResponse(AbstractModel):
    """DescribeCdnIp response structure.

    """

    def __init__(self):
        """
        :param Ips: Node ownership details
        :type Ips: list of CdnIp
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Ips = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Ips") is not None:
            self.Ips = []
            for item in params.get("Ips"):
                obj = CdnIp()
                obj._deserialize(item)
                self.Ips.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDomainsConfigRequest(AbstractModel):
    """DescribeDomainsConfig request structure.

    """

    def __init__(self):
        """
        :param Offset: Offset for paged queries. Default value: 0 (the first page).
        :type Offset: int
        :param Limit: Limit on paged queries. Default value: 100. Maximum value: 1000.
        :type Limit: int
        :param Filters: Query condition filter, complex type.
        :type Filters: list of DomainFilter
        :param Sort: Sorting rules
        :type Sort: :class:`tencentcloud.cdn.v20180606.models.Sort`
        """
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.Sort = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = DomainFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        if params.get("Sort") is not None:
            self.Sort = Sort()
            self.Sort._deserialize(params.get("Sort"))


class DescribeDomainsConfigResponse(AbstractModel):
    """DescribeDomainsConfig response structure.

    """

    def __init__(self):
        """
        :param Domains: List of domain names
        :type Domains: list of DetailDomain
        :param TotalNumber: The number of domain names that matched the query conditions
Used for paged queries
        :type TotalNumber: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Domains = None
        self.TotalNumber = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Domains") is not None:
            self.Domains = []
            for item in params.get("Domains"):
                obj = DetailDomain()
                obj._deserialize(item)
                self.Domains.append(obj)
        self.TotalNumber = params.get("TotalNumber")
        self.RequestId = params.get("RequestId")


class DescribeDomainsRequest(AbstractModel):
    """DescribeDomains request structure.

    """

    def __init__(self):
        """
        :param Offset: Offset for paged queries. Default value: 0 (the first page).
        :type Offset: int
        :param Limit: Limit on paged queries. Default value: 100. Maximum value: 1000.
        :type Limit: int
        :param Filters: Query condition filter, complex type.
        :type Filters: list of DomainFilter
        """
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = DomainFilter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeDomainsResponse(AbstractModel):
    """DescribeDomains response structure.

    """

    def __init__(self):
        """
        :param Domains: List of domain names
        :type Domains: list of BriefDomain
        :param TotalNumber: The number of domain names that matched the query conditions
Used for paged queries
        :type TotalNumber: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Domains = None
        self.TotalNumber = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Domains") is not None:
            self.Domains = []
            for item in params.get("Domains"):
                obj = BriefDomain()
                obj._deserialize(item)
                self.Domains.append(obj)
        self.TotalNumber = params.get("TotalNumber")
        self.RequestId = params.get("RequestId")


class DescribeIpVisitRequest(AbstractModel):
    """DescribeIpVisit request structure.

    """

    def __init__(self):
        """
        :param StartTime: Query start time, such as 2018-09-04 10:40:10; the returned result is later than or equal to the specified time.
According to the specified time granularity, forward rounding is applied; for example, if the query start time is 2018-09-04 10:40:10 and the query time granularity is 5 minutes, the time for the first returned entry will be 2018-09-04 10:40:00.
        :type StartTime: str
        :param EndTime: Query end time, such as 2018-09-04 10:40:10; the returned result is earlier than or equal to the specified time.
According to the specified time granularity, forward rounding is applied; for example, if the query start time is 2018-09-04 10:40:10 and the query time granularity is 5 minutes, the time for the last returned entry will be 2018-09-04 10:40:00.
        :type EndTime: str
        :param Domains: Specifies the list of domain names to be queried; up to 30 domain names can be queried at a time.
        :type Domains: list of str
        :param Project: Specifies the project ID to be queried, which can be viewed [here](https://console.cloud.tencent.com/project)
Please note that if domain names are specified, this parameter will be ignored.
        :type Project: int
        :param Interval: Time granularity, which can be:
5min: 5 minutes. If the query period is within 24 hours, `5min` will be used by default.
day: 1 day. If the query period is longer than 24 hours, `day` will be used by default.
        :type Interval: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Domains = None
        self.Project = None
        self.Interval = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Domains = params.get("Domains")
        self.Project = params.get("Project")
        self.Interval = params.get("Interval")


class DescribeIpVisitResponse(AbstractModel):
    """DescribeIpVisit response structure.

    """

    def __init__(self):
        """
        :param Interval: Time granularity of data statistics, which supports 5min (5 minutes) and day (1 day).
        :type Interval: str
        :param Data: Origin-pull data details of each resource.
        :type Data: list of ResourceData
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Interval = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Interval = params.get("Interval")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ResourceData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMapInfoRequest(AbstractModel):
    """DescribeMapInfo request structure.

    """

    def __init__(self):
        """
        :param Name: Query type:
`isp`: queries ISP codes
`district`: queries codes of provinces (Mainland China) or countries/regions (outside Mainland China)
        :type Name: str
        """
        self.Name = None


    def _deserialize(self, params):
        self.Name = params.get("Name")


class DescribeMapInfoResponse(AbstractModel):
    """DescribeMapInfo response structure.

    """

    def __init__(self):
        """
        :param MapInfoList: Array of mappings.
        :type MapInfoList: list of MapInfo
        :param ServerRegionRelation: The relationship between server region ID and sub-region ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ServerRegionRelation: list of RegionMapRelation
        :param ClientRegionRelation: The relationship between client region ID and sub-region ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClientRegionRelation: list of RegionMapRelation
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.MapInfoList = None
        self.ServerRegionRelation = None
        self.ClientRegionRelation = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MapInfoList") is not None:
            self.MapInfoList = []
            for item in params.get("MapInfoList"):
                obj = MapInfo()
                obj._deserialize(item)
                self.MapInfoList.append(obj)
        if params.get("ServerRegionRelation") is not None:
            self.ServerRegionRelation = []
            for item in params.get("ServerRegionRelation"):
                obj = RegionMapRelation()
                obj._deserialize(item)
                self.ServerRegionRelation.append(obj)
        if params.get("ClientRegionRelation") is not None:
            self.ClientRegionRelation = []
            for item in params.get("ClientRegionRelation"):
                obj = RegionMapRelation()
                obj._deserialize(item)
                self.ClientRegionRelation.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeOriginDataRequest(AbstractModel):
    """DescribeOriginData request structure.

    """

    def __init__(self):
        """
        :param StartTime: Query start time, such as 2018-09-04 10:40:00; the returned result is later than or equal to the specified time.
According to the specified time granularity, forward rounding is applied; for example, if the query end time is 2018-09-04 10:40:00 and the query time granularity is 1 hour, the time for the first returned entry will be 2018-09-04 10:00:00.
The gap between the start time and end time should be less than or equal to 90 days.
        :type StartTime: str
        :param EndTime: Query end time, such as 2018-09-04 10:40:00; the returned result is earlier than or equal to the specified time.
According to the specified time granularity, forward rounding is applied; for example, if the query start time is 2018-09-04 10:40:00 and the query time granularity is 1 hour, the time for the last returned entry will be 2018-09-04 10:00:00.
The gap between the start time and end time should be less than or equal to 90 days.
        :type EndTime: str
        :param Metric: Specifies the query metric, which can be:
flux: origin-pull traffic (in bytes)
bandwidth: origin-pull bandwidth (in bps)
request: number of origin-pull requests
failRequest: number of failed origin-pull requests
failRate: origin-pull failure rate (in %)
statusCode: origin-pull status code. The aggregate data for 2xx, 3xx, 4xx, and 5xx origin-pull status codes will be returned (in entries)
2xx: Returns the aggregate list of 2xx origin-pull status codes and the data for origin-pull status codes starting with 2 (in entries)
3xx: Returns the aggregate list of 3xx origin-pull status codes and the data for origin-pull status codes starting with 3 (in entries)
4xx: Returns the aggregate list of 4xx origin-pull status codes and the data for origin-pull status codes starting with 4 (in entries)
5xx: Returns the aggregate list of 5xx origin-pull status codes and the data for origin-pull status codes starting with 5 (in entries)
It is supported to specify a status code for query. The return will be empty if the status code has never been generated.
        :type Metric: str
        :param Domains: Specifies the list of domain names to be queried; up to 30 domain names can be queried at a time.
        :type Domains: list of str
        :param Project: Specifies the project ID to be queried, which can be viewed [here](https://console.cloud.tencent.com/project)
Please note that if domain names are specified, this parameter will be ignored.
        :type Project: int
        :param Interval: Time granularity; valid values:
`min`: data with 1-minute granularity is returned when the queried period is no longer than 24 hours. This value is not supported if the service region you want to query is outside Mainland China;
`5min`: data with 5-minute granularity is returned when the queried period is no longer than 31 days;
`hour`: data with 1-hour granularity is returned when the queried period is no longer than 31 days;
`day`: data with 1-day granularity is returned when the queried period is longer than 31 days.
        :type Interval: str
        :param Detail: The aggregate data for multiple domain names is returned by default (false) when multiple `Domains` are passed in.
You can set it to true to return the details for each Domain (the statusCode metric is currently not supported)
        :type Detail: bool
        :param Area: Specifies a service region. If this value is left blank, CDN data within Mainland China will be queried.
`mainland`: specifies to query CDN data within Mainland China;
`overseas`: specifies to query CDN data outside Mainland China.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Metric = None
        self.Domains = None
        self.Project = None
        self.Interval = None
        self.Detail = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Metric = params.get("Metric")
        self.Domains = params.get("Domains")
        self.Project = params.get("Project")
        self.Interval = params.get("Interval")
        self.Detail = params.get("Detail")
        self.Area = params.get("Area")


class DescribeOriginDataResponse(AbstractModel):
    """DescribeOriginData response structure.

    """

    def __init__(self):
        """
        :param Interval: Time granularity of data statistics, which supports min (1 minute), 5min (5 minutes), hour (1 hour), and day (1 day).
        :type Interval: str
        :param Data: Origin-pull data details of each resource.
        :type Data: list of ResourceOriginData
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Interval = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Interval = params.get("Interval")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ResourceOriginData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePayTypeRequest(AbstractModel):
    """DescribePayType request structure.

    """

    def __init__(self):
        """
        :param Area: Specifies a service region.
`mainland`: queries billing methods within Mainland China;
`overseas`: queries billing methods outside Mainland China.
Default value: `mainland`.
        :type Area: str
        """
        self.Area = None


    def _deserialize(self, params):
        self.Area = params.get("Area")


class DescribePayTypeResponse(AbstractModel):
    """DescribePayType response structure.

    """

    def __init__(self):
        """
        :param PayType: Billing modes:
`flux`: bill-by-traffic
`bandwidth`: bill-by-bandwidth
When you switch the billing mode for a daily-billing-cycle account, if there is bandwidth usage on the day, this field indicates the billing mode that will take effect on the next day; otherwise, it indicates the billing mode that has already taken effect
        :type PayType: str
        :param BillingCycle: Billing cycle:
day: daily settlement
month: monthly settlement
        :type BillingCycle: str
        :param StatType: Billing method:
monthMax: billed by the monthly average of daily peak traffic (monthly settlement)
day95: billed by the daily 95th percentile bandwidth (monthly settlement)
month95: billed by the monthly 95th percentile bandwidth (monthly settlement)
sum: billed by the total traffic (daily or monthly settlement)
max: billed by the peak bandwidth (daily settlement)
        :type StatType: str
        :param RegionType: Billing method outside Mainland China:
`all`: unified billing for all regions
`multiple`: separate billing for different regions
        :type RegionType: str
        :param CurrentPayType: Currently billing mode in effect:
`flux`: bill-by-traffic
`bandwidth`: bill-by-bandwidth
        :type CurrentPayType: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PayType = None
        self.BillingCycle = None
        self.StatType = None
        self.RegionType = None
        self.CurrentPayType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PayType = params.get("PayType")
        self.BillingCycle = params.get("BillingCycle")
        self.StatType = params.get("StatType")
        self.RegionType = params.get("RegionType")
        self.CurrentPayType = params.get("CurrentPayType")
        self.RequestId = params.get("RequestId")


class DescribePurgeTasksRequest(AbstractModel):
    """DescribePurgeTasks request structure.

    """

    def __init__(self):
        """
        :param PurgeType: Specifies a purge type:
`url`: URL purge record
`path`: Directory purge record
        :type PurgeType: str
        :param StartTime: Specifies the starting time of the period you want to query, such as `2018-08-08 00:00:00`
        :type StartTime: str
        :param EndTime: Specifies the end time of the period you want to query, such as 2018-08-08 23:59:59
        :type EndTime: str
        :param TaskId: Specifies a task ID when you want to query by task ID.
You must specify either a task ID or a starting time for your query.
        :type TaskId: str
        :param Offset: Offset for paged queries. Default value: 0 (the first page)
        :type Offset: int
        :param Limit: Limit on paged queries. Default value: 20
        :type Limit: int
        :param Keyword: You can filter the results by domain name or a complete URL beginning with `http(s)://`
        :type Keyword: str
        :param Status: Specifies a task state for your query:
`fail`: purge failed
`done`: purge succeeded
`process`: purge in progress
        :type Status: str
        :param Area: Specifies a purge region for your query:
`mainland`: within Mainland China
`overseas`: outside Mainland China
`global`: global
        :type Area: str
        """
        self.PurgeType = None
        self.StartTime = None
        self.EndTime = None
        self.TaskId = None
        self.Offset = None
        self.Limit = None
        self.Keyword = None
        self.Status = None
        self.Area = None


    def _deserialize(self, params):
        self.PurgeType = params.get("PurgeType")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.TaskId = params.get("TaskId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Keyword = params.get("Keyword")
        self.Status = params.get("Status")
        self.Area = params.get("Area")


class DescribePurgeTasksResponse(AbstractModel):
    """DescribePurgeTasks response structure.

    """

    def __init__(self):
        """
        :param PurgeLogs: Detailed purge record.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PurgeLogs: list of PurgeTask
        :param TotalCount: Total number of tasks, which is used for pagination.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PurgeLogs = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PurgeLogs") is not None:
            self.PurgeLogs = []
            for item in params.get("PurgeLogs"):
                obj = PurgeTask()
                obj._deserialize(item)
                self.PurgeLogs.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribePushTasksRequest(AbstractModel):
    """DescribePushTasks request structure.

    """

    def __init__(self):
        """
        :param StartTime: Starting time, such as `2018-08-08 00:00:00`
        :type StartTime: str
        :param EndTime: End time, such as `2018-08-08 23:59:59`
        :type EndTime: str
        :param TaskId: Specifies a task ID for your query.
You must specify either a task ID or a starting time.
        :type TaskId: str
        :param Keyword: Specifies a keyword for your query. Please enter a domain name or a complete URL beginning with `http(s)://`
        :type Keyword: str
        :param Offset: Offset for paged queries. Default value: 0 (the first page)
        :type Offset: int
        :param Limit: Limit on paged queries. Default value: 20
        :type Limit: int
        :param Area: Specifies a region for your query:
`mainland`: within Mainland China
`overseas`: outside Mainland China
`global`: global
        :type Area: str
        :param Status: Specifies a task state for your query:
`fail`: prefetch failed
`done`: prefetch succeeded
`process`: prefetch in progress
        :type Status: str
        """
        self.StartTime = None
        self.EndTime = None
        self.TaskId = None
        self.Keyword = None
        self.Offset = None
        self.Limit = None
        self.Area = None
        self.Status = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.TaskId = params.get("TaskId")
        self.Keyword = params.get("Keyword")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Area = params.get("Area")
        self.Status = params.get("Status")


class DescribePushTasksResponse(AbstractModel):
    """DescribePushTasks response structure.

    """

    def __init__(self):
        """
        :param PushLogs: Prefetch history
Note: This field may return null, indicating that no valid values can be obtained.
        :type PushLogs: list of PushTask
        :param TotalCount: Total number of tasks, which is used for pagination.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PushLogs = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PushLogs") is not None:
            self.PushLogs = []
            for item in params.get("PushLogs"):
                obj = PushTask()
                obj._deserialize(item)
                self.PushLogs.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeUrlViolationsRequest(AbstractModel):
    """DescribeUrlViolations request structure.

    """

    def __init__(self):
        """
        :param Offset: Offset for paged queries. Default value: 0 (the first page).
        :type Offset: int
        :param Limit: Limit on paged queries. Default value: 100.
        :type Limit: int
        :param Domains: Specified domain name query
        :type Domains: list of str
        """
        self.Offset = None
        self.Limit = None
        self.Domains = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Domains = params.get("Domains")


class DescribeUrlViolationsResponse(AbstractModel):
    """DescribeUrlViolations response structure.

    """

    def __init__(self):
        """
        :param UrlRecordList: Details of violating URLs
Note: this field may return null, indicating that no valid values can be obtained.
        :type UrlRecordList: list of ViolationUrl
        :param TotalCount: Total number of records, which is used for pagination.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.UrlRecordList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("UrlRecordList") is not None:
            self.UrlRecordList = []
            for item in params.get("UrlRecordList"):
                obj = ViolationUrl()
                obj._deserialize(item)
                self.UrlRecordList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DetailDomain(AbstractModel):
    """Detailed configuration information for CDN domain names.

    """

    def __init__(self):
        """
        :param ResourceId: Domain name ID.
        :type ResourceId: str
        :param AppId: Tencent Cloud account ID.
        :type AppId: int
        :param Domain: Accelerated domain name.
        :type Domain: str
        :param Cname: Domain name CNAME.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Cname: str
        :param Status: Domain name status. pending: under review; rejected: review failed; processing: review succeeded and under deployment; online: enabled; offline: disabled; deleted: deleted.
        :type Status: str
        :param ProjectId: Project ID.
        :type ProjectId: int
        :param ServiceType: Domain name business type. web: static acceleration; download: download acceleration; media: streaming media acceleration.
        :type ServiceType: str
        :param CreateTime: Domain name creation time.
        :type CreateTime: str
        :param UpdateTime: Domain name update time.
        :type UpdateTime: str
        :param Origin: Origin server configuration.
        :type Origin: :class:`tencentcloud.cdn.v20180606.models.Origin`
        :param IpFilter: IP blacklist/whitelist configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IpFilter: :class:`tencentcloud.cdn.v20180606.models.IpFilter`
        :param IpFreqLimit: IP access limit configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IpFreqLimit: :class:`tencentcloud.cdn.v20180606.models.IpFreqLimit`
        :param StatusCodeCache: Status code cache configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type StatusCodeCache: :class:`tencentcloud.cdn.v20180606.models.StatusCodeCache`
        :param Compression: Smart compression configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Compression: :class:`tencentcloud.cdn.v20180606.models.Compression`
        :param BandwidthAlert: Bandwidth cap configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type BandwidthAlert: :class:`tencentcloud.cdn.v20180606.models.BandwidthAlert`
        :param RangeOriginPull: Range origin-pull configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RangeOriginPull: :class:`tencentcloud.cdn.v20180606.models.RangeOriginPull`
        :param FollowRedirect: 301 and 302 automatic origin-pull follow-redirect configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FollowRedirect: :class:`tencentcloud.cdn.v20180606.models.FollowRedirect`
        :param ErrorPage: Error code redirect configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ErrorPage`
        :param RequestHeader: Origin-pull request header configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RequestHeader: :class:`tencentcloud.cdn.v20180606.models.RequestHeader`
        :param ResponseHeader: Origin server response header configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResponseHeader: :class:`tencentcloud.cdn.v20180606.models.ResponseHeader`
        :param DownstreamCapping: Download speed configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DownstreamCapping: :class:`tencentcloud.cdn.v20180606.models.DownstreamCapping`
        :param CacheKey: Node cache configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CacheKey: :class:`tencentcloud.cdn.v20180606.models.CacheKey`
        :param ResponseHeaderCache: Follows origin server cache header configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResponseHeaderCache: :class:`tencentcloud.cdn.v20180606.models.ResponseHeaderCache`
        :param VideoSeek: Video dragging configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VideoSeek: :class:`tencentcloud.cdn.v20180606.models.VideoSeek`
        :param Cache: Cache rules configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Cache: :class:`tencentcloud.cdn.v20180606.models.Cache`
        :param OriginPullOptimization: Cross-border optimization configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OriginPullOptimization: :class:`tencentcloud.cdn.v20180606.models.OriginPullOptimization`
        :param Https: HTTPS configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Https: :class:`tencentcloud.cdn.v20180606.models.Https`
        :param Authentication: Timestamp hotlink protection configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Authentication: :class:`tencentcloud.cdn.v20180606.models.Authentication`
        :param Seo: SEO configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Seo: :class:`tencentcloud.cdn.v20180606.models.Seo`
        :param Disable: Domain name block status, including normal, overdue, quota, malicious, ddos, idle, unlicensed, capping, and readonly.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Disable: str
        :param ForceRedirect: Access protocol forced redirect configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ForceRedirect: :class:`tencentcloud.cdn.v20180606.models.ForceRedirect`
        :param Referer: Hotlink protection configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Referer: :class:`tencentcloud.cdn.v20180606.models.Referer`
        :param MaxAge: Browser cache rules configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxAge: :class:`tencentcloud.cdn.v20180606.models.MaxAge`
        :param Ipv6: IPv6 configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Ipv6: :class:`tencentcloud.cdn.v20180606.models.Ipv6`
        :param Compatibility: Whether it is compatible with configurations in old versions.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Compatibility: :class:`tencentcloud.cdn.v20180606.models.Compatibility`
        :param SpecificConfig: Specific configuration by region.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SpecificConfig: :class:`tencentcloud.cdn.v20180606.models.SpecificConfig`
        :param Area: Acceleration region, including mainland, overseas, and global.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Area: str
        :param Readonly: Domain name lock status. normal: not locked; mainland: locked in mainland China; overseas: locked outside mainland China; global: locked globally.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Readonly: str
        :param OriginPullTimeout: Origin-pull timeout configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type OriginPullTimeout: :class:`tencentcloud.cdn.v20180606.models.OriginPullTimeout`
        """
        self.ResourceId = None
        self.AppId = None
        self.Domain = None
        self.Cname = None
        self.Status = None
        self.ProjectId = None
        self.ServiceType = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Origin = None
        self.IpFilter = None
        self.IpFreqLimit = None
        self.StatusCodeCache = None
        self.Compression = None
        self.BandwidthAlert = None
        self.RangeOriginPull = None
        self.FollowRedirect = None
        self.ErrorPage = None
        self.RequestHeader = None
        self.ResponseHeader = None
        self.DownstreamCapping = None
        self.CacheKey = None
        self.ResponseHeaderCache = None
        self.VideoSeek = None
        self.Cache = None
        self.OriginPullOptimization = None
        self.Https = None
        self.Authentication = None
        self.Seo = None
        self.Disable = None
        self.ForceRedirect = None
        self.Referer = None
        self.MaxAge = None
        self.Ipv6 = None
        self.Compatibility = None
        self.SpecificConfig = None
        self.Area = None
        self.Readonly = None
        self.OriginPullTimeout = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.AppId = params.get("AppId")
        self.Domain = params.get("Domain")
        self.Cname = params.get("Cname")
        self.Status = params.get("Status")
        self.ProjectId = params.get("ProjectId")
        self.ServiceType = params.get("ServiceType")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        if params.get("IpFilter") is not None:
            self.IpFilter = IpFilter()
            self.IpFilter._deserialize(params.get("IpFilter"))
        if params.get("IpFreqLimit") is not None:
            self.IpFreqLimit = IpFreqLimit()
            self.IpFreqLimit._deserialize(params.get("IpFreqLimit"))
        if params.get("StatusCodeCache") is not None:
            self.StatusCodeCache = StatusCodeCache()
            self.StatusCodeCache._deserialize(params.get("StatusCodeCache"))
        if params.get("Compression") is not None:
            self.Compression = Compression()
            self.Compression._deserialize(params.get("Compression"))
        if params.get("BandwidthAlert") is not None:
            self.BandwidthAlert = BandwidthAlert()
            self.BandwidthAlert._deserialize(params.get("BandwidthAlert"))
        if params.get("RangeOriginPull") is not None:
            self.RangeOriginPull = RangeOriginPull()
            self.RangeOriginPull._deserialize(params.get("RangeOriginPull"))
        if params.get("FollowRedirect") is not None:
            self.FollowRedirect = FollowRedirect()
            self.FollowRedirect._deserialize(params.get("FollowRedirect"))
        if params.get("ErrorPage") is not None:
            self.ErrorPage = ErrorPage()
            self.ErrorPage._deserialize(params.get("ErrorPage"))
        if params.get("RequestHeader") is not None:
            self.RequestHeader = RequestHeader()
            self.RequestHeader._deserialize(params.get("RequestHeader"))
        if params.get("ResponseHeader") is not None:
            self.ResponseHeader = ResponseHeader()
            self.ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("DownstreamCapping") is not None:
            self.DownstreamCapping = DownstreamCapping()
            self.DownstreamCapping._deserialize(params.get("DownstreamCapping"))
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("ResponseHeaderCache") is not None:
            self.ResponseHeaderCache = ResponseHeaderCache()
            self.ResponseHeaderCache._deserialize(params.get("ResponseHeaderCache"))
        if params.get("VideoSeek") is not None:
            self.VideoSeek = VideoSeek()
            self.VideoSeek._deserialize(params.get("VideoSeek"))
        if params.get("Cache") is not None:
            self.Cache = Cache()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("OriginPullOptimization") is not None:
            self.OriginPullOptimization = OriginPullOptimization()
            self.OriginPullOptimization._deserialize(params.get("OriginPullOptimization"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        if params.get("Authentication") is not None:
            self.Authentication = Authentication()
            self.Authentication._deserialize(params.get("Authentication"))
        if params.get("Seo") is not None:
            self.Seo = Seo()
            self.Seo._deserialize(params.get("Seo"))
        self.Disable = params.get("Disable")
        if params.get("ForceRedirect") is not None:
            self.ForceRedirect = ForceRedirect()
            self.ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Referer") is not None:
            self.Referer = Referer()
            self.Referer._deserialize(params.get("Referer"))
        if params.get("MaxAge") is not None:
            self.MaxAge = MaxAge()
            self.MaxAge._deserialize(params.get("MaxAge"))
        if params.get("Ipv6") is not None:
            self.Ipv6 = Ipv6()
            self.Ipv6._deserialize(params.get("Ipv6"))
        if params.get("Compatibility") is not None:
            self.Compatibility = Compatibility()
            self.Compatibility._deserialize(params.get("Compatibility"))
        if params.get("SpecificConfig") is not None:
            self.SpecificConfig = SpecificConfig()
            self.SpecificConfig._deserialize(params.get("SpecificConfig"))
        self.Area = params.get("Area")
        self.Readonly = params.get("Readonly")
        if params.get("OriginPullTimeout") is not None:
            self.OriginPullTimeout = OriginPullTimeout()
            self.OriginPullTimeout._deserialize(params.get("OriginPullTimeout"))


class DisableCachesRequest(AbstractModel):
    """DisableCaches request structure.

    """

    def __init__(self):
        """
        :param Urls: List of URLs to be blocked
Up to 100 entries can be submitted at a time and 3,000 entries per day.
        :type Urls: list of str
        """
        self.Urls = None


    def _deserialize(self, params):
        self.Urls = params.get("Urls")


class DisableCachesResponse(AbstractModel):
    """DisableCaches response structure.

    """

    def __init__(self):
        """
        :param CacheOptResult: Submission result
Note: This field may return null, indicating that no valid values can be obtained.
        :type CacheOptResult: :class:`tencentcloud.cdn.v20180606.models.CacheOptResult`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CacheOptResult = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CacheOptResult") is not None:
            self.CacheOptResult = CacheOptResult()
            self.CacheOptResult._deserialize(params.get("CacheOptResult"))
        self.RequestId = params.get("RequestId")


class DomainFilter(AbstractModel):
    """Filter conditions for domain name query.

    """

    def __init__(self):
        """
        :param Name: Filter field name, the list supported is as follows:
- origin: master origin server.
- domain: domain name.
- resourceId: domain name id.
- status: domain name status, online, offline, or processing.
- serviceType: service type, web, download, or media.
- projectId: project ID.
- domainType: master origin server type, cname indicates external origin, COS indicates COS origin.
- fullUrlCache: full-path cache, which can be on or off.
- https: whether to configure HTTPS, which can be on, off or processing.
- originPullProtocol: origin-pull protocol type. It supports HTTP, follow, or HTTPS.
- tagKey: tag key.
        :type Name: str
        :param Value: Filter field value.
        :type Value: list of str
        :param Fuzzy: Whether to enable fuzzy query. Only origin or domain is supported for the filter field name.
When fuzzy query is enabled, the maximum Value length is 1. When fuzzy query is disabled, the maximum Value length is 5.
        :type Fuzzy: bool
        """
        self.Name = None
        self.Value = None
        self.Fuzzy = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        self.Fuzzy = params.get("Fuzzy")


class DomainLog(AbstractModel):
    """Details about a log package download link

    """

    def __init__(self):
        """
        :param StartTime: Starting time of the log package
        :type StartTime: str
        :param EndTime: End time of the log package
        :type EndTime: str
        :param LogPath: Log package download link
        :type LogPath: str
        :param Area: Acceleration region corresponding to the log package
`mainland`: within Mainland China
`overseas`: outside Mainland China
        :type Area: str
        :param LogName: Log package filename
        :type LogName: str
        """
        self.StartTime = None
        self.EndTime = None
        self.LogPath = None
        self.Area = None
        self.LogName = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.LogPath = params.get("LogPath")
        self.Area = params.get("Area")
        self.LogName = params.get("LogName")


class DownstreamCapping(AbstractModel):
    """Single link downstream speed limit configuration. It is disabled by default.

    """

    def __init__(self):
        """
        :param Switch: Downstream speed configuration switch
on: enabled
off: disabled
        :type Switch: str
        :param CappingRules: Downstream speed limiting rules
Note: this field may return null, indicating that no valid values can be obtained.
        :type CappingRules: list of CappingRule
        """
        self.Switch = None
        self.CappingRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("CappingRules") is not None:
            self.CappingRules = []
            for item in params.get("CappingRules"):
                obj = CappingRule()
                obj._deserialize(item)
                self.CappingRules.append(obj)


class EnableCachesRequest(AbstractModel):
    """EnableCaches request structure.

    """

    def __init__(self):
        """
        :param Urls: List of unblocked URLs
        :type Urls: list of str
        """
        self.Urls = None


    def _deserialize(self, params):
        self.Urls = params.get("Urls")


class EnableCachesResponse(AbstractModel):
    """EnableCaches response structure.

    """

    def __init__(self):
        """
        :param CacheOptResult: Result list
Note: This field may return null, indicating that no valid values can be obtained.
        :type CacheOptResult: :class:`tencentcloud.cdn.v20180606.models.CacheOptResult`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CacheOptResult = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CacheOptResult") is not None:
            self.CacheOptResult = CacheOptResult()
            self.CacheOptResult._deserialize(params.get("CacheOptResult"))
        self.RequestId = params.get("RequestId")


class ErrorPage(AbstractModel):
    """Status code redirect configuration. It is disabled by default. (This feature is in beta test and not fully available yet.)

    """

    def __init__(self):
        """
        :param Switch: Status code redirect configuration switch
on: enabled
off: disabled
Note: this field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        :param PageRules: Status code redirect rules configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type PageRules: list of ErrorPageRule
        """
        self.Switch = None
        self.PageRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("PageRules") is not None:
            self.PageRules = []
            for item in params.get("PageRules"):
                obj = ErrorPageRule()
                obj._deserialize(item)
                self.PageRules.append(obj)


class ErrorPageRule(AbstractModel):
    """Status code redirect rules configuration

    """

    def __init__(self):
        """
        :param StatusCode: Status code
It supports 400, 403, 404, 500.
        :type StatusCode: int
        :param RedirectCode: Redirect status code settings
It supports 301 or 302.
        :type RedirectCode: int
        :param RedirectUrl: Redirect URL
It requires a full redirect path, such as https://www.test.com/error.html.
        :type RedirectUrl: str
        """
        self.StatusCode = None
        self.RedirectCode = None
        self.RedirectUrl = None


    def _deserialize(self, params):
        self.StatusCode = params.get("StatusCode")
        self.RedirectCode = params.get("RedirectCode")
        self.RedirectUrl = params.get("RedirectUrl")


class FollowRedirect(AbstractModel):
    """301/302 automatic origin-pull follow-redirect configuration. It is disabled by default.

    """

    def __init__(self):
        """
        :param Switch: Origin-pull follow-redirect switch
on: enabled
off: disabled
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class ForceRedirect(AbstractModel):
    """Access protocol forced redirect configuration. It is disabled by default.

    """

    def __init__(self):
        """
        :param Switch: Access forced redirect configuration switch
on: enabled
off: disabled
Note: this field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        :param RedirectType: Access forced redirect types
http: forced HTTP redirect
https: forced HTTPS redirect
Note: this field may return null, indicating that no valid values can be obtained.
        :type RedirectType: str
        :param RedirectStatusCode: Status code returned for forced redirect 
It supports 301, 302.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RedirectStatusCode: int
        """
        self.Switch = None
        self.RedirectType = None
        self.RedirectStatusCode = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.RedirectType = params.get("RedirectType")
        self.RedirectStatusCode = params.get("RedirectStatusCode")


class GetDisableRecordsRequest(AbstractModel):
    """GetDisableRecords request structure.

    """

    def __init__(self):
        """
        :param StartTime: Starting time, such as `2018-12-12 10:24:00`
        :type StartTime: str
        :param EndTime: End time, such as 2018-12-14 10:24:00
        :type EndTime: str
        :param Url: Specifies the URL to be queried
        :type Url: str
        :param Status: Current URL status
disable: The URL remains disabled, and accessing it will return an error 403
enable: The URL is enabled (unblocked) and can be normally accessed
        :type Status: str
        :param Offset: Offset for paged queries. Default value: 0 (the first page)
        :type Offset: int
        :param Limit: Limit on paged queries. Default value: 20
        :type Limit: int
        """
        self.StartTime = None
        self.EndTime = None
        self.Url = None
        self.Status = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Url = params.get("Url")
        self.Status = params.get("Status")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class GetDisableRecordsResponse(AbstractModel):
    """GetDisableRecords response structure.

    """

    def __init__(self):
        """
        :param UrlRecordList: Blocking history
Note: This field may return null, indicating that no valid values can be obtained.
        :type UrlRecordList: list of UrlRecord
        :param TotalCount: Total number of tasks, which is used for pagination
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.UrlRecordList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("UrlRecordList") is not None:
            self.UrlRecordList = []
            for item in params.get("UrlRecordList"):
                obj = UrlRecord()
                obj._deserialize(item)
                self.UrlRecordList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class HttpHeaderPathRule(AbstractModel):
    """HTTP header setting rules. Up to 100 entries can be set.

    """

    def __init__(self):
        """
        :param HeaderMode: HTTP header setting method
add: add header. If a header exists, then there will be a repeated header.
set: only supports origin-pull header configuration. If a header exists, it will be overwritten. If one does not exist, then the header will be added.
del: delete header
Note: this field may return null, indicating that no valid values can be obtained.
        :type HeaderMode: str
        :param HeaderName: HTTP header name. Up to 100 characters can be set.
Note: this field may return null, indicating that no valid values can be obtained.
        :type HeaderName: str
        :param HeaderValue: HTTP header value. Up to 1000 characters can be set.
It is not required when Mode is del
It is required when Mode is add/set
Note: this field may return null, indicating that no valid values can be obtained.
        :type HeaderValue: str
        :param RuleType: Rule types:
all: all files take effect
file: specified file suffixes take effect
directory: specified paths take effect
path: specified absolute paths take effect
Note: this field may return null, indicating that no valid values can be obtained.
        :type RuleType: str
        :param RulePaths: Matching content under the corresponding types for RuleType:
For "all", enter an asterisk (*).
For "file", enter the suffix, such as jpg, txt.
For "directory", enter the path, such as /xxx/test/.
For "path", enter the corresponding absolute path, such as /xxx/test.html.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RulePaths: list of str
        """
        self.HeaderMode = None
        self.HeaderName = None
        self.HeaderValue = None
        self.RuleType = None
        self.RulePaths = None


    def _deserialize(self, params):
        self.HeaderMode = params.get("HeaderMode")
        self.HeaderName = params.get("HeaderName")
        self.HeaderValue = params.get("HeaderValue")
        self.RuleType = params.get("RuleType")
        self.RulePaths = params.get("RulePaths")


class Https(AbstractModel):
    """Domain name HTTPS acceleration configuration. It is disabled by default.

    """

    def __init__(self):
        """
        :param Switch: HTTPS configuration switch
on: enabled
off: disabled
Note: this field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        :param Http2: HTTP2 configuration switch
on: enabled
off: disabled
The first time HTTPS acceleration is enabled, it will enable HTTP2 configuration by default.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Http2: str
        :param OcspStapling: OCSP configuration switch
on: enabled
off: disabled
It is disabled by default
Note: this field may return null, indicating that no valid values can be obtained.
        :type OcspStapling: str
        :param VerifyClient: Client certificate authentication feature
on: enabled
off: disabled
It is disabled by default. If it is enabled, you need to upload the client certificate information. This configuration is in beta test and not fully available yet.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VerifyClient: str
        :param CertInfo: Server certificate configuration information
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertInfo: :class:`tencentcloud.cdn.v20180606.models.ServerCert`
        :param ClientCertInfo: Client certificate configuration information
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClientCertInfo: :class:`tencentcloud.cdn.v20180606.models.ClientCert`
        :param Spdy: Spdy configuration switch
on: enabled
off: disabled
It is disabled by default
Note: this field may return null, indicating that no valid values can be obtained.
        :type Spdy: str
        :param SslStatus: HTTPS certificate deployment status
closed: already closed
deploying: being deployed
deployed: successfully deployed
failed: deployment failed
Note: this field may return null, indicating that no valid values can be obtained.
        :type SslStatus: str
        """
        self.Switch = None
        self.Http2 = None
        self.OcspStapling = None
        self.VerifyClient = None
        self.CertInfo = None
        self.ClientCertInfo = None
        self.Spdy = None
        self.SslStatus = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Http2 = params.get("Http2")
        self.OcspStapling = params.get("OcspStapling")
        self.VerifyClient = params.get("VerifyClient")
        if params.get("CertInfo") is not None:
            self.CertInfo = ServerCert()
            self.CertInfo._deserialize(params.get("CertInfo"))
        if params.get("ClientCertInfo") is not None:
            self.ClientCertInfo = ClientCert()
            self.ClientCertInfo._deserialize(params.get("ClientCertInfo"))
        self.Spdy = params.get("Spdy")
        self.SslStatus = params.get("SslStatus")


class IpFilter(AbstractModel):
    """IP blacklist/whitelist configuration. It is disabled by default.

    """

    def __init__(self):
        """
        :param Switch: IP blacklist/whitelist configuration switch
on: enabled
off: disabled
        :type Switch: str
        :param FilterType: IP blacklist/whitelist type
whitelist: whitelist
blacklist: blacklist
Note: this field may return null, indicating that no valid values can be obtained.
        :type FilterType: str
        :param Filters: IP blacklist/whitelist list
It supports IPs in X.X.X.X format, or /8, /16, /24 format IP ranges.
Up to 50 whitelists or blacklists can be entered
Note: this field may return null, indicating that no valid values can be obtained.
        :type Filters: list of str
        """
        self.Switch = None
        self.FilterType = None
        self.Filters = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.FilterType = params.get("FilterType")
        self.Filters = params.get("Filters")


class IpFreqLimit(AbstractModel):
    """Access limit configuration for a single IP of a single node. It is disabled by default.

    """

    def __init__(self):
        """
        :param Switch: IP access limit configuration switch
on: enabled
off: disabled
        :type Switch: str
        :param Qps: Sets the number limit of request per second
514 will be returned to the requests that exceed the limit
Note: this field may return null, indicating that no valid values can be obtained.
        :type Qps: int
        """
        self.Switch = None
        self.Qps = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Qps = params.get("Qps")


class Ipv6(AbstractModel):
    """IPv6 activation configurations, which cannot be changed.

    """

    def __init__(self):
        """
        :param Switch: Whether to enable the IPv6 feature for a domain name, which can be on or off.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class ListTopDataRequest(AbstractModel):
    """ListTopData request structure.

    """

    def __init__(self):
        """
        :param StartTime: Query start date. Example: 2018-09-09.
It only supports data query at daily granularity. The date information in the input parameter is the start date.
Returns data generated at or after 00:00:00 on the start date.
It only supports querying of data within 90 days.
        :type StartTime: str
        :param EndTime: Query end date. Example: 2018-09-10
It only supports data query at daily granularity. The date information in the input parameter is the end date.
Returns data generated before or at 23:59:59 on the end date.
EndTime must be greater than or equal to StartTime
        :type EndTime: str
        :param Metric: Objects to be sorted. Valid values:
`url`: sorts access URLs with query string parameters included. Supported filters are `flux` and `request`.
`path`: sorts access URLs with query string parameters excluded. Supported filters are `flux` and `request`. You need to be whitelisted before using this feature.
`district`: sorts provinces or countries/regions. Supported filters are `flux` and `request`.
`isp`: sorts ISPs. Supported filters are `flux` and `request`.
`host`: sorts domain name access data. Supported filters are `flux`, `request`, `bandwidth`, `fluxHitRate`, `2XX`, `3XX`, `4XX`, `5XX` and `statusCode`.
`originHost`: sorts by domain name origin-pull data. Supported filters are `flux`, `request`, `bandwidth`, `origin_2XX`, `origin_3XX`, `oringin_4XX`, `origin_5XX` and `OriginStatusCode`
        :type Metric: str
        :param Filter: Metric name used for sorting:
flux: If Metric is `host`, it indicates the access traffic; if Metric is `originHost`, it indicates the origin-pull traffic.
bandwidth: If Metric is `host`, it indicates the access bandwidth; if Metric is `originHost`, it indicates the origin-pull bandwidth.
request: If Metric is `host`, it indicates the number of access requests; if Metric is `originHost`, it indicates the number of origin-pull requests.
fluxHitRate: Average traffic hit rate
2XX: access 2XX status code
3XX: access 3XX status code
4XX: access 4XX status code
5XX: access 5XX status code
origin_2XX: origin-pull 2XX status code
origin_3XX: origin-pull 3XX status code
origin_4XX: origin-pull 4XX status code
origin_5XX: origin-pull 5XX status code
statusCode: statistics of a specific access status code which is specified in the `Code` parameter.
OriginStatusCode: statistics of a specific origin-pull status code which is specified in the `Code` parameter.
        :type Filter: str
        :param Domains: Specifies the list of domain names to be queried; up to 30 domain names can be queried at a time.
        :type Domains: list of str
        :param Project: Specifies the project ID to be queried, which can be viewed [here](https://console.cloud.tencent.com/project)
Please note that if domain names are specified, this parameter will be ignored.
        :type Project: int
        :param Detail: Default value: `false`, indicating that results for all domain names are returned together when you query multiple domain names.
If `Metric` is `Url`, `Path`, `District`, or `Isp` and `Filter` is `flux` or `request`, you can set this parameter to `true`, indicating that results for each domain name are returned.
        :type Detail: bool
        :param Code: When Filter is `statusCode` or `OriginStatusCode`, enter a code to query and sort results.
        :type Code: str
        :param Area: Specifies a service region for the query. If it is left blank, CDN data within Mainland China will be queried.
`mainland`: specifies to query CDN data within Mainland China;
`overseas`: specifies to query CDN data outside Mainland China. Supported metrics are `url`, `district`, `host`, and `originHost`. If `Metric` is `originHost`, supported filters are `flux`, `request`, and `bandwidth`.
        :type Area: str
        :param AreaType: Specifies a region type for the query. If it is left blank, data on the service region will be queried. This parameter is only valid when `Area` is `overseas` and `Metric` is `District` or `Host`.
`server`: specifies to query data on the service region where Tencent Cloud CDN nodes are located;
`client`: specifies to query data on the client region where the request devices are located; if `Metric` is `Host`, supported filters are `flux`, `request`, and `bandwidth`.
        :type AreaType: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Metric = None
        self.Filter = None
        self.Domains = None
        self.Project = None
        self.Detail = None
        self.Code = None
        self.Area = None
        self.AreaType = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Metric = params.get("Metric")
        self.Filter = params.get("Filter")
        self.Domains = params.get("Domains")
        self.Project = params.get("Project")
        self.Detail = params.get("Detail")
        self.Code = params.get("Code")
        self.Area = params.get("Area")
        self.AreaType = params.get("AreaType")


class ListTopDataResponse(AbstractModel):
    """ListTopData response structure.

    """

    def __init__(self):
        """
        :param Data: Top access data details of each resource
        :type Data: list of TopData
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TopData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class MainlandConfig(AbstractModel):
    """Specific configuration for domain names in the mainland China. Specific configuration by region. UpdateDomainConfig API only supports modification of some region configurations. For compatibility with configuration of older versions, this type will list out all the configuration differences that may exist with old versions. The supported configuration list is as follows:
    + Authentication
    + BandwidthAlert
    + ErrorPage
    + IpFilter
    + Origin
    + Referer

    """

    def __init__(self):
        """
        :param Authentication: Timestamp hotlink protection configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Authentication: :class:`tencentcloud.cdn.v20180606.models.Authentication`
        :param BandwidthAlert: Bandwidth cap configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type BandwidthAlert: :class:`tencentcloud.cdn.v20180606.models.BandwidthAlert`
        :param Cache: Cache rules configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Cache: :class:`tencentcloud.cdn.v20180606.models.Cache`
        :param CacheKey: Cache configurations.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CacheKey: :class:`tencentcloud.cdn.v20180606.models.CacheKey`
        :param Compression: Smart compression configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Compression: :class:`tencentcloud.cdn.v20180606.models.Compression`
        :param DownstreamCapping: Download speed limit configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DownstreamCapping: :class:`tencentcloud.cdn.v20180606.models.DownstreamCapping`
        :param ErrorPage: Error code redirect configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ErrorPage`
        :param FollowRedirect: 301 and 302 automatic origin-pull follow-redirect configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FollowRedirect: :class:`tencentcloud.cdn.v20180606.models.FollowRedirect`
        :param ForceRedirect: Access protocol forced redirect configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ForceRedirect: :class:`tencentcloud.cdn.v20180606.models.ForceRedirect`
        :param Https: HTTPS configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Https: :class:`tencentcloud.cdn.v20180606.models.Https`
        :param IpFilter: IP blacklist/whitelist configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IpFilter: :class:`tencentcloud.cdn.v20180606.models.IpFilter`
        :param IpFreqLimit: IP access limit configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IpFreqLimit: :class:`tencentcloud.cdn.v20180606.models.IpFreqLimit`
        :param MaxAge: Browser cache rules configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxAge: :class:`tencentcloud.cdn.v20180606.models.MaxAge`
        :param Origin: Origin server configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Origin: :class:`tencentcloud.cdn.v20180606.models.Origin`
        :param OriginPullOptimization: Cross-border optimization configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OriginPullOptimization: :class:`tencentcloud.cdn.v20180606.models.OriginPullOptimization`
        :param RangeOriginPull: Range origin-pull configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RangeOriginPull: :class:`tencentcloud.cdn.v20180606.models.RangeOriginPull`
        :param Referer: Hotlink protection configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Referer: :class:`tencentcloud.cdn.v20180606.models.Referer`
        :param RequestHeader: Origin-pull request header configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RequestHeader: :class:`tencentcloud.cdn.v20180606.models.RequestHeader`
        :param ResponseHeader: Origin server response header configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResponseHeader: :class:`tencentcloud.cdn.v20180606.models.ResponseHeader`
        :param ResponseHeaderCache: Follows origin server cache header configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResponseHeaderCache: :class:`tencentcloud.cdn.v20180606.models.ResponseHeaderCache`
        :param Seo: SEO configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Seo: :class:`tencentcloud.cdn.v20180606.models.Seo`
        :param ServiceType: Domain name business type. web: static acceleration; download: download acceleration; media: streaming media acceleration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceType: str
        :param StatusCodeCache: Status code cache configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type StatusCodeCache: :class:`tencentcloud.cdn.v20180606.models.StatusCodeCache`
        :param VideoSeek: Video dragging configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VideoSeek: :class:`tencentcloud.cdn.v20180606.models.VideoSeek`
        """
        self.Authentication = None
        self.BandwidthAlert = None
        self.Cache = None
        self.CacheKey = None
        self.Compression = None
        self.DownstreamCapping = None
        self.ErrorPage = None
        self.FollowRedirect = None
        self.ForceRedirect = None
        self.Https = None
        self.IpFilter = None
        self.IpFreqLimit = None
        self.MaxAge = None
        self.Origin = None
        self.OriginPullOptimization = None
        self.RangeOriginPull = None
        self.Referer = None
        self.RequestHeader = None
        self.ResponseHeader = None
        self.ResponseHeaderCache = None
        self.Seo = None
        self.ServiceType = None
        self.StatusCodeCache = None
        self.VideoSeek = None


    def _deserialize(self, params):
        if params.get("Authentication") is not None:
            self.Authentication = Authentication()
            self.Authentication._deserialize(params.get("Authentication"))
        if params.get("BandwidthAlert") is not None:
            self.BandwidthAlert = BandwidthAlert()
            self.BandwidthAlert._deserialize(params.get("BandwidthAlert"))
        if params.get("Cache") is not None:
            self.Cache = Cache()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("Compression") is not None:
            self.Compression = Compression()
            self.Compression._deserialize(params.get("Compression"))
        if params.get("DownstreamCapping") is not None:
            self.DownstreamCapping = DownstreamCapping()
            self.DownstreamCapping._deserialize(params.get("DownstreamCapping"))
        if params.get("ErrorPage") is not None:
            self.ErrorPage = ErrorPage()
            self.ErrorPage._deserialize(params.get("ErrorPage"))
        if params.get("FollowRedirect") is not None:
            self.FollowRedirect = FollowRedirect()
            self.FollowRedirect._deserialize(params.get("FollowRedirect"))
        if params.get("ForceRedirect") is not None:
            self.ForceRedirect = ForceRedirect()
            self.ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        if params.get("IpFilter") is not None:
            self.IpFilter = IpFilter()
            self.IpFilter._deserialize(params.get("IpFilter"))
        if params.get("IpFreqLimit") is not None:
            self.IpFreqLimit = IpFreqLimit()
            self.IpFreqLimit._deserialize(params.get("IpFreqLimit"))
        if params.get("MaxAge") is not None:
            self.MaxAge = MaxAge()
            self.MaxAge._deserialize(params.get("MaxAge"))
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        if params.get("OriginPullOptimization") is not None:
            self.OriginPullOptimization = OriginPullOptimization()
            self.OriginPullOptimization._deserialize(params.get("OriginPullOptimization"))
        if params.get("RangeOriginPull") is not None:
            self.RangeOriginPull = RangeOriginPull()
            self.RangeOriginPull._deserialize(params.get("RangeOriginPull"))
        if params.get("Referer") is not None:
            self.Referer = Referer()
            self.Referer._deserialize(params.get("Referer"))
        if params.get("RequestHeader") is not None:
            self.RequestHeader = RequestHeader()
            self.RequestHeader._deserialize(params.get("RequestHeader"))
        if params.get("ResponseHeader") is not None:
            self.ResponseHeader = ResponseHeader()
            self.ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("ResponseHeaderCache") is not None:
            self.ResponseHeaderCache = ResponseHeaderCache()
            self.ResponseHeaderCache._deserialize(params.get("ResponseHeaderCache"))
        if params.get("Seo") is not None:
            self.Seo = Seo()
            self.Seo._deserialize(params.get("Seo"))
        self.ServiceType = params.get("ServiceType")
        if params.get("StatusCodeCache") is not None:
            self.StatusCodeCache = StatusCodeCache()
            self.StatusCodeCache._deserialize(params.get("StatusCodeCache"))
        if params.get("VideoSeek") is not None:
            self.VideoSeek = VideoSeek()
            self.VideoSeek._deserialize(params.get("VideoSeek"))


class MapInfo(AbstractModel):
    """Mapping between a name and an ID

    """

    def __init__(self):
        """
        :param Id: Object ID
        :type Id: int
        :param Name: Object name
        :type Name: str
        """
        self.Id = None
        self.Name = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")


class MaxAge(AbstractModel):
    """Browser cache rule configuration. It is used to set the MaxAge default value and is disabled by default. (This feature is in beta test and not fully available yet.)

    """

    def __init__(self):
        """
        :param Switch: Browser cache configuration switch
on: enabled
off: disabled
Note: this field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        :param MaxAgeRules: MaxAge rule
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxAgeRules: list of MaxAgeRule
        """
        self.Switch = None
        self.MaxAgeRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("MaxAgeRules") is not None:
            self.MaxAgeRules = []
            for item in params.get("MaxAgeRules"):
                obj = MaxAgeRule()
                obj._deserialize(item)
                self.MaxAgeRules.append(obj)


class MaxAgeRule(AbstractModel):
    """MaxAge rules configuration

    """

    def __init__(self):
        """
        :param MaxAgeType: Rule types:
all: all files take effect
file: specified file suffixes take effect
directory: specified paths take effect
path: specified absolute paths take effect
        :type MaxAgeType: str
        :param MaxAgeContents: Matching content under the corresponding types for MaxAgeType:
For "all", enter an asterisk (*).
For "file", enter the suffix, such as jpg, txt.
For "directory", enter the path, such as /xxx/test/.
For "path", enter the corresponding absolute path, such as /xxx/test.html.
        :type MaxAgeContents: list of str
        :param MaxAgeTime: MaxAge time settings (in seconds)
        :type MaxAgeTime: int
        """
        self.MaxAgeType = None
        self.MaxAgeContents = None
        self.MaxAgeTime = None


    def _deserialize(self, params):
        self.MaxAgeType = params.get("MaxAgeType")
        self.MaxAgeContents = params.get("MaxAgeContents")
        self.MaxAgeTime = params.get("MaxAgeTime")


class Origin(AbstractModel):
    """Origin server configuration complex type. It supports the following configurations:
    + Origin server specified as a single domain name
    + Origin server specified as multiple IPs. Supported port range: 1-65535; Supported weight range: 1-100. Format: IP:Port:Weight.
    + Origin-pull domain name configuration
    + Cloud Object Storage (COS) is specified as origin server
    + Hot backup origin server is specified as a single domain name
    + Hot backup origin server is specified as multiple IPs. Supported port range: 1-65535. At present, weight configuration is not supported.
    + Hot backup origin server origin-pull domain name configuration

    """

    def __init__(self):
        """
        :param Origins: Master origin server list
When modifying the origin server, you need to enter the corresponding OriginType.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Origins: list of str
        :param OriginType: Master origin server type
The following types are supported in input parameters:
domain: domain name type
cos: COS origin
ip: IP list is used as origin server
ipv6: origin server list is a single IPv6 address
ip_ipv6: origin server list is multiple IPv4 addresses and an IPv6 address
The following types of output parameters are added:
image: cloud Infinite origin
ftp: historical FTP origin, which is no longer maintained.
When modifying Origins, you need to enter the corresponding OriginType.
The IPv6 feature is not fully available yet. To use this feature, you need to apply for it first.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OriginType: str
        :param ServerName: Host header used when pulling the master origin server. If the Host header is not entered, it will be the acceleration domain name by default.
If a wildcard domain name is accessed, then the Host header is the sub-domain name during the access by default.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServerName: str
        :param CosPrivateAccess: When OriginType is COS, you can specify whether to allow access to private buckets.
Note: to enable this configuration, you need to authorize the CDN to access this private bucket first.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CosPrivateAccess: str
        :param OriginPullProtocol: Origin-pull protocol configuration
http: forced HTTP origin-pull
follow: protocol follow origin-pull
https: forced HTTPS origin-pull. It only supports origin server port 443 for origin-pull.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OriginPullProtocol: str
        :param BackupOrigins: Backup origin server list
When modifying the backup origin server, you need to enter the corresponding BackupOriginType.
Note: this field may return null, indicating that no valid values can be obtained.
        :type BackupOrigins: list of str
        :param BackupOriginType: Backup origin server type, which supports the following types:
domain: domain name type
ip: IP list is used as origin server
When modifying BackupOrigins, you need to enter the corresponding BackupOriginType.
Note: this field may return null, indicating that no valid values can be obtained.
        :type BackupOriginType: str
        :param BackupServerName: Host header used when pulling the backup origin server. If the Host header is not entered, it will be the ServerName of master origin server by default.
Note: this field may return null, indicating that no valid values can be obtained.
        :type BackupServerName: str
        """
        self.Origins = None
        self.OriginType = None
        self.ServerName = None
        self.CosPrivateAccess = None
        self.OriginPullProtocol = None
        self.BackupOrigins = None
        self.BackupOriginType = None
        self.BackupServerName = None


    def _deserialize(self, params):
        self.Origins = params.get("Origins")
        self.OriginType = params.get("OriginType")
        self.ServerName = params.get("ServerName")
        self.CosPrivateAccess = params.get("CosPrivateAccess")
        self.OriginPullProtocol = params.get("OriginPullProtocol")
        self.BackupOrigins = params.get("BackupOrigins")
        self.BackupOriginType = params.get("BackupOriginType")
        self.BackupServerName = params.get("BackupServerName")


class OriginPullOptimization(AbstractModel):
    """Cross-border origin-pull optimization configuration. It is disabled by default. (This feature is in beta test and not fully available yet.)

    """

    def __init__(self):
        """
        :param Switch: Cross-border origin-pull optimization configuration switch
on: enabled
off: disabled
        :type Switch: str
        :param OptimizationType: Cross-border types
OVToCN: origin-pull from outside mainland China to inside mainland China
CNToOV: origin-pull from inside mainland China to outside mainland China
Note: this field may return null, indicating that no valid values can be obtained.
        :type OptimizationType: str
        """
        self.Switch = None
        self.OptimizationType = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.OptimizationType = params.get("OptimizationType")


class OriginPullTimeout(AbstractModel):
    """Origin-pull timeout configuration

    """

    def __init__(self):
        """
        :param ConnectTimeout: The origin-pull connection timeout (in seconds). Valid range: 5-60.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ConnectTimeout: int
        :param ReceiveTimeout: The origin-pull receipt timeout (in seconds). Valid range: 10-60.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ReceiveTimeout: int
        """
        self.ConnectTimeout = None
        self.ReceiveTimeout = None


    def _deserialize(self, params):
        self.ConnectTimeout = params.get("ConnectTimeout")
        self.ReceiveTimeout = params.get("ReceiveTimeout")


class OverseaConfig(AbstractModel):
    """Specific configuration for domain names outside mainland China. UpdateDomainConfig API only supports modification of some region configurations. For compatibility with configuration of older versions, this type will list out all the configuration differences that may exist with old versions. The supported configuration list is as follows:
    + Authentication
    + BandwidthAlert
    + ErrorPage
    + IpFilter
    + Origin
    + Referer

    """

    def __init__(self):
        """
        :param Authentication: Timestamp hotlink protection configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Authentication: :class:`tencentcloud.cdn.v20180606.models.Authentication`
        :param BandwidthAlert: Bandwidth cap configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type BandwidthAlert: :class:`tencentcloud.cdn.v20180606.models.BandwidthAlert`
        :param Cache: Cache rules configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Cache: :class:`tencentcloud.cdn.v20180606.models.Cache`
        :param CacheKey: Cache configurations.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CacheKey: :class:`tencentcloud.cdn.v20180606.models.CacheKey`
        :param Compression: Smart compression configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Compression: :class:`tencentcloud.cdn.v20180606.models.Compression`
        :param DownstreamCapping: Download speed limit configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DownstreamCapping: :class:`tencentcloud.cdn.v20180606.models.DownstreamCapping`
        :param ErrorPage: Error code redirect configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ErrorPage`
        :param FollowRedirect: 301 and 302 automatic origin-pull follow-redirect configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FollowRedirect: :class:`tencentcloud.cdn.v20180606.models.FollowRedirect`
        :param ForceRedirect: Access protocol forced redirect configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ForceRedirect: :class:`tencentcloud.cdn.v20180606.models.ForceRedirect`
        :param Https: HTTPS configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Https: :class:`tencentcloud.cdn.v20180606.models.Https`
        :param IpFilter: IP blacklist/whitelist configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IpFilter: :class:`tencentcloud.cdn.v20180606.models.IpFilter`
        :param IpFreqLimit: IP access limit configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IpFreqLimit: :class:`tencentcloud.cdn.v20180606.models.IpFreqLimit`
        :param MaxAge: Browser cache rules configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxAge: :class:`tencentcloud.cdn.v20180606.models.MaxAge`
        :param Origin: Origin server configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Origin: :class:`tencentcloud.cdn.v20180606.models.Origin`
        :param OriginPullOptimization: Cross-border optimization configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OriginPullOptimization: :class:`tencentcloud.cdn.v20180606.models.OriginPullOptimization`
        :param RangeOriginPull: Range origin-pull configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RangeOriginPull: :class:`tencentcloud.cdn.v20180606.models.RangeOriginPull`
        :param Referer: Hotlink protection configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Referer: :class:`tencentcloud.cdn.v20180606.models.Referer`
        :param RequestHeader: Origin-pull request header configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RequestHeader: :class:`tencentcloud.cdn.v20180606.models.RequestHeader`
        :param ResponseHeader: Origin server response header configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResponseHeader: :class:`tencentcloud.cdn.v20180606.models.ResponseHeader`
        :param ResponseHeaderCache: Follows origin server cache header configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResponseHeaderCache: :class:`tencentcloud.cdn.v20180606.models.ResponseHeaderCache`
        :param Seo: SEO configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Seo: :class:`tencentcloud.cdn.v20180606.models.Seo`
        :param ServiceType: Domain name business type. web: static acceleration; download: download acceleration; media: streaming media acceleration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceType: str
        :param StatusCodeCache: Status code cache configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type StatusCodeCache: :class:`tencentcloud.cdn.v20180606.models.StatusCodeCache`
        :param VideoSeek: Video dragging configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VideoSeek: :class:`tencentcloud.cdn.v20180606.models.VideoSeek`
        """
        self.Authentication = None
        self.BandwidthAlert = None
        self.Cache = None
        self.CacheKey = None
        self.Compression = None
        self.DownstreamCapping = None
        self.ErrorPage = None
        self.FollowRedirect = None
        self.ForceRedirect = None
        self.Https = None
        self.IpFilter = None
        self.IpFreqLimit = None
        self.MaxAge = None
        self.Origin = None
        self.OriginPullOptimization = None
        self.RangeOriginPull = None
        self.Referer = None
        self.RequestHeader = None
        self.ResponseHeader = None
        self.ResponseHeaderCache = None
        self.Seo = None
        self.ServiceType = None
        self.StatusCodeCache = None
        self.VideoSeek = None


    def _deserialize(self, params):
        if params.get("Authentication") is not None:
            self.Authentication = Authentication()
            self.Authentication._deserialize(params.get("Authentication"))
        if params.get("BandwidthAlert") is not None:
            self.BandwidthAlert = BandwidthAlert()
            self.BandwidthAlert._deserialize(params.get("BandwidthAlert"))
        if params.get("Cache") is not None:
            self.Cache = Cache()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("Compression") is not None:
            self.Compression = Compression()
            self.Compression._deserialize(params.get("Compression"))
        if params.get("DownstreamCapping") is not None:
            self.DownstreamCapping = DownstreamCapping()
            self.DownstreamCapping._deserialize(params.get("DownstreamCapping"))
        if params.get("ErrorPage") is not None:
            self.ErrorPage = ErrorPage()
            self.ErrorPage._deserialize(params.get("ErrorPage"))
        if params.get("FollowRedirect") is not None:
            self.FollowRedirect = FollowRedirect()
            self.FollowRedirect._deserialize(params.get("FollowRedirect"))
        if params.get("ForceRedirect") is not None:
            self.ForceRedirect = ForceRedirect()
            self.ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        if params.get("IpFilter") is not None:
            self.IpFilter = IpFilter()
            self.IpFilter._deserialize(params.get("IpFilter"))
        if params.get("IpFreqLimit") is not None:
            self.IpFreqLimit = IpFreqLimit()
            self.IpFreqLimit._deserialize(params.get("IpFreqLimit"))
        if params.get("MaxAge") is not None:
            self.MaxAge = MaxAge()
            self.MaxAge._deserialize(params.get("MaxAge"))
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        if params.get("OriginPullOptimization") is not None:
            self.OriginPullOptimization = OriginPullOptimization()
            self.OriginPullOptimization._deserialize(params.get("OriginPullOptimization"))
        if params.get("RangeOriginPull") is not None:
            self.RangeOriginPull = RangeOriginPull()
            self.RangeOriginPull._deserialize(params.get("RangeOriginPull"))
        if params.get("Referer") is not None:
            self.Referer = Referer()
            self.Referer._deserialize(params.get("Referer"))
        if params.get("RequestHeader") is not None:
            self.RequestHeader = RequestHeader()
            self.RequestHeader._deserialize(params.get("RequestHeader"))
        if params.get("ResponseHeader") is not None:
            self.ResponseHeader = ResponseHeader()
            self.ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("ResponseHeaderCache") is not None:
            self.ResponseHeaderCache = ResponseHeaderCache()
            self.ResponseHeaderCache._deserialize(params.get("ResponseHeaderCache"))
        if params.get("Seo") is not None:
            self.Seo = Seo()
            self.Seo._deserialize(params.get("Seo"))
        self.ServiceType = params.get("ServiceType")
        if params.get("StatusCodeCache") is not None:
            self.StatusCodeCache = StatusCodeCache()
            self.StatusCodeCache._deserialize(params.get("StatusCodeCache"))
        if params.get("VideoSeek") is not None:
            self.VideoSeek = VideoSeek()
            self.VideoSeek._deserialize(params.get("VideoSeek"))


class PurgePathCacheRequest(AbstractModel):
    """PurgePathCache request structure.

    """

    def __init__(self):
        """
        :param Paths: List of directories. The protocol header such as "http://" or "https://" needs to be included.
        :type Paths: list of str
        :param FlushType: Purge type:
`flush`: purges updated resources
`delete`: purges all resources
        :type FlushType: str
        """
        self.Paths = None
        self.FlushType = None


    def _deserialize(self, params):
        self.Paths = params.get("Paths")
        self.FlushType = params.get("FlushType")


class PurgePathCacheResponse(AbstractModel):
    """PurgePathCache response structure.

    """

    def __init__(self):
        """
        :param TaskId: Purge task ID. Directories submitted in one request share a task ID.
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class PurgeTask(AbstractModel):
    """Purge task details.

    """

    def __init__(self):
        """
        :param TaskId: Purge task ID
        :type TaskId: str
        :param Url: Purged URL
        :type Url: str
        :param Status: Purge task status
`fail`: purge failed
`done`: purge succeeded
`process`: purge in progress
        :type Status: str
        :param PurgeType: Purge type
`url`: URL purge
`path`: directory purge
        :type PurgeType: str
        :param FlushType: Purge method
`flush`: purges updated resources; this type is available only for directory purges
`delete`: purges all resources
        :type FlushType: str
        :param CreateTime: Purge task submission time
        :type CreateTime: str
        """
        self.TaskId = None
        self.Url = None
        self.Status = None
        self.PurgeType = None
        self.FlushType = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Url = params.get("Url")
        self.Status = params.get("Status")
        self.PurgeType = params.get("PurgeType")
        self.FlushType = params.get("FlushType")
        self.CreateTime = params.get("CreateTime")


class PurgeUrlsCacheRequest(AbstractModel):
    """PurgeUrlsCache request structure.

    """

    def __init__(self):
        """
        :param Urls: List of URLs. The protocol header such as "http://" or "https://" needs to be included.
        :type Urls: list of str
        """
        self.Urls = None


    def _deserialize(self, params):
        self.Urls = params.get("Urls")


class PurgeUrlsCacheResponse(AbstractModel):
    """PurgeUrlsCache response structure.

    """

    def __init__(self):
        """
        :param TaskId: Purge task ID. URLs submitted in one request share a task ID.
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class PushTask(AbstractModel):
    """Prefetch task details.

    """

    def __init__(self):
        """
        :param TaskId: Prefetch task ID
        :type TaskId: str
        :param Url: Prefetched URL
        :type Url: str
        :param Status: Prefetch task status
`fail`: prefetch failed
`done`: prefetch succeeded
`process`: prefetch in progress
        :type Status: str
        :param Percent: Prefetch progress in percentage
        :type Percent: int
        :param CreateTime: Prefetch task submission time
        :type CreateTime: str
        :param Area: Prefetch region
`mainland`: within Mainland China
`overseas`: outside Mainland China
`global`: global
        :type Area: str
        :param UpdateTime: Prefetch task update time
Note: this field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        """
        self.TaskId = None
        self.Url = None
        self.Status = None
        self.Percent = None
        self.CreateTime = None
        self.Area = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Url = params.get("Url")
        self.Status = params.get("Status")
        self.Percent = params.get("Percent")
        self.CreateTime = params.get("CreateTime")
        self.Area = params.get("Area")
        self.UpdateTime = params.get("UpdateTime")


class PushUrlsCacheRequest(AbstractModel):
    """PushUrlsCache request structure.

    """

    def __init__(self):
        """
        :param Urls: List of URLs. The protocol header such as "http://" or "https://" needs to be included.
        :type Urls: list of str
        :param UserAgent: Specifies the User-Agent header of an HTTP prefetch request when it is forwarded to the origin server
Default value: `TencentCdn`
        :type UserAgent: str
        :param Area: Destination region for the prefetch
`mainland`: prefetches resources to nodes within Mainland China
`overseas`: prefetches resources to nodes outside Mainland China
`global`: prefetches resources to global nodes
Default value: `mainland`. You can prefetch a URL to nodes in a region provided that CDN service has been enabled for the domain name in the URL in the region.
        :type Area: str
        """
        self.Urls = None
        self.UserAgent = None
        self.Area = None


    def _deserialize(self, params):
        self.Urls = params.get("Urls")
        self.UserAgent = params.get("UserAgent")
        self.Area = params.get("Area")


class PushUrlsCacheResponse(AbstractModel):
    """PushUrlsCache response structure.

    """

    def __init__(self):
        """
        :param TaskId: ID of the submitted task
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class RangeOriginPull(AbstractModel):
    """Range GETs configuration which is enabled by default

    """

    def __init__(self):
        """
        :param Switch: Range GETs configuration switch
on: enabled
off: disabled
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class Referer(AbstractModel):
    """Referer blacklist/whitelist configuration. It is disabled by default.

    """

    def __init__(self):
        """
        :param Switch: Referer blacklist/whitelist configuration switch
on: enabled
off: disabled
        :type Switch: str
        :param RefererRules: Referer blacklist/whitelist configuration rule
Note: this field may return null, indicating that no valid values can be obtained.
        :type RefererRules: list of RefererRule
        """
        self.Switch = None
        self.RefererRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("RefererRules") is not None:
            self.RefererRules = []
            for item in params.get("RefererRules"):
                obj = RefererRule()
                obj._deserialize(item)
                self.RefererRules.append(obj)


class RefererRule(AbstractModel):
    """Referer blacklist/whitelist configuration rules, which is effective for specific resources.

    """

    def __init__(self):
        """
        :param RuleType: Rule types:
all: all files take effect
file: specified file suffixes take effect
directory: specified paths take effect
path: specified absolute paths take effect
        :type RuleType: str
        :param RulePaths: Matching content under the corresponding types for RuleType:
For "all", enter an asterisk (*).
For "file", enter the suffix, such as jpg, txt.
For "directory", enter the path, such as /xxx/test/.
For "path", enter the corresponding absolute path, such as /xxx/test.html.
        :type RulePaths: list of str
        :param RefererType: Referer configuration types
whitelist: whitelist
blacklist: blacklist
        :type RefererType: str
        :param Referers: Referer content list
        :type Referers: list of str
        :param AllowEmpty: Whether to allow empty referer
true: allow empty referer
false: do not allow empty referer
        :type AllowEmpty: bool
        """
        self.RuleType = None
        self.RulePaths = None
        self.RefererType = None
        self.Referers = None
        self.AllowEmpty = None


    def _deserialize(self, params):
        self.RuleType = params.get("RuleType")
        self.RulePaths = params.get("RulePaths")
        self.RefererType = params.get("RefererType")
        self.Referers = params.get("Referers")
        self.AllowEmpty = params.get("AllowEmpty")


class RegionMapRelation(AbstractModel):
    """Association between a region ID and sub-region IDs.

    """

    def __init__(self):
        """
        :param RegionId: Region ID
        :type RegionId: int
        :param SubRegionIdList: List of sub-region IDs
        :type SubRegionIdList: list of int
        """
        self.RegionId = None
        self.SubRegionIdList = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.SubRegionIdList = params.get("SubRegionIdList")


class RequestHeader(AbstractModel):
    """Custom request header configuration. It is disabled by default.

    """

    def __init__(self):
        """
        :param Switch: Custom request header configuration switch
on: enabled
off: disabled
        :type Switch: str
        :param HeaderRules: Custom request header configuration rules
Note: this field may return null, indicating that no valid values can be obtained.
        :type HeaderRules: list of HttpHeaderPathRule
        """
        self.Switch = None
        self.HeaderRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("HeaderRules") is not None:
            self.HeaderRules = []
            for item in params.get("HeaderRules"):
                obj = HttpHeaderPathRule()
                obj._deserialize(item)
                self.HeaderRules.append(obj)


class ResourceData(AbstractModel):
    """This API is used to query an object and its access details

    """

    def __init__(self):
        """
        :param Resource: Resource name, which is classified as follows based on different query conditions:
A specific domain name: This indicates the details of this domain name
multiDomains: This indicates the aggregate details of multiple domain names
Project ID: This displays the ID of the specifically queried project
all: This indicates the details at the account level
        :type Resource: str
        :param CdnData: Data details of a resource
        :type CdnData: list of CdnData
        """
        self.Resource = None
        self.CdnData = None


    def _deserialize(self, params):
        self.Resource = params.get("Resource")
        if params.get("CdnData") is not None:
            self.CdnData = []
            for item in params.get("CdnData"):
                obj = CdnData()
                obj._deserialize(item)
                self.CdnData.append(obj)


class ResourceOriginData(AbstractModel):
    """This API is used to query an object and its origin-pull details

    """

    def __init__(self):
        """
        :param Resource: Resource name, which is classified as follows based on different query conditions:
A specific domain name: This indicates the details of this domain name
multiDomains: This indicates the aggregate details of multiple domain names
Project ID: This displays the ID of the specifically queried project
all: This indicates the details at the account level
        :type Resource: str
        :param OriginData: Origin-pull data details
        :type OriginData: list of CdnData
        """
        self.Resource = None
        self.OriginData = None


    def _deserialize(self, params):
        self.Resource = params.get("Resource")
        if params.get("OriginData") is not None:
            self.OriginData = []
            for item in params.get("OriginData"):
                obj = CdnData()
                obj._deserialize(item)
                self.OriginData.append(obj)


class ResponseHeader(AbstractModel):
    """Custom response header configuration. It is disabled by default.

    """

    def __init__(self):
        """
        :param Switch: Custom response header switch
on: enabled
off: disabled
        :type Switch: str
        :param HeaderRules: Custom response header rules
Note: this field may return null, indicating that no valid values can be obtained.
        :type HeaderRules: list of HttpHeaderPathRule
        """
        self.Switch = None
        self.HeaderRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("HeaderRules") is not None:
            self.HeaderRules = []
            for item in params.get("HeaderRules"):
                obj = HttpHeaderPathRule()
                obj._deserialize(item)
                self.HeaderRules.append(obj)


class ResponseHeaderCache(AbstractModel):
    """Origin server header cache configuration. It is enabled by default and caches all the header information.

    """

    def __init__(self):
        """
        :param Switch: Origin server header cache switch
on: enabled
off: disabled
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class Seo(AbstractModel):
    """SEO configuration. It is disabled by default.

    """

    def __init__(self):
        """
        :param Switch: SEO configuration switch
on: enabled
off: disabled
Note: this field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class ServerCert(AbstractModel):
    """HTTPS acceleration server certificate configuration:
    + It supports deployment with certificates that are being hosted by the SSL Certificate Services
    + It supports uploading certificates of PEM format for deployment
    Note: when uploading certificates of PEM format, the Base64 encoding is required.

    """

    def __init__(self):
        """
        :param CertId: Server certificate ID
It is auto-generated when the certificate is being hosted by the SSL Certificate Service
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertId: str
        :param CertName: Server certificate name
It is auto-generated when the certificate is being hosted by the SSL Certificate Service
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertName: str
        :param Certificate: Server certificate information
It is required when uploading an external certificate, which should contain the complete certificate chain.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Certificate: str
        :param PrivateKey: Server key information
It is required when uploading an external certificate.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PrivateKey: str
        :param ExpireTime: Certificate expiration time
When it is used as an input parameter, it can be left blank.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param DeployTime: Certificate issuance time
When it is used as an input parameter, it can be left blank.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeployTime: str
        :param Message: Certificate remarks
Note: this field may return null, indicating that no valid values can be obtained.
        :type Message: str
        """
        self.CertId = None
        self.CertName = None
        self.Certificate = None
        self.PrivateKey = None
        self.ExpireTime = None
        self.DeployTime = None
        self.Message = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.CertName = params.get("CertName")
        self.Certificate = params.get("Certificate")
        self.PrivateKey = params.get("PrivateKey")
        self.ExpireTime = params.get("ExpireTime")
        self.DeployTime = params.get("DeployTime")
        self.Message = params.get("Message")


class SimpleCache(AbstractModel):
    """Cache configuration basic version
    The cache expiration time for all files is 30 days by default.
    Static acceleration type domain names .php, .jsp, .asp, and .aspx are not cached by default
    Note: this version does not support setting cache expiration rules if the origin server does not return max-age

    """

    def __init__(self):
        """
        :param CacheRules: Cache expiration time rules
Note: this field may return null, indicating that no valid values can be obtained.
        :type CacheRules: list of SimpleCacheRule
        :param FollowOrigin: Follows origin server Cache-Control: max-age configurations
on: enabled
off: disabled
If it is enabled, resources that do not match CacheRules rules will be cached by the node according to the max-age value returned by the origin server. Resources that match CacheRules rules will be cached on the node according to the cache expiration time set in CacheRules.
It conflicts with CompareMaxAge. They cannot be enabled at the same time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FollowOrigin: str
        :param IgnoreCacheControl: Forced cache
on: enabled
off: disabled
It is disabled by default. If it is enabled, no-store and no-cache resources returned from the origin server will be cached according to CacheRules rules.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IgnoreCacheControl: str
        :param IgnoreSetCookie: Ignores the Set-Cookie header of the origin server
on: enabled
off: disabled
It is disabled by default
Note: this field may return null, indicating that no valid values can be obtained.
        :type IgnoreSetCookie: str
        :param CompareMaxAge: Advanced cache expiration configuration. If it is enabled, the max-age value returned by the origin server will be compared with the cache expiration time set in CacheRules, and the smallest value will be cached on the node.
on: enabled
off: disabled
It is disabled by default
Note: this field may return null, indicating that no valid values can be obtained.
        :type CompareMaxAge: str
        """
        self.CacheRules = None
        self.FollowOrigin = None
        self.IgnoreCacheControl = None
        self.IgnoreSetCookie = None
        self.CompareMaxAge = None


    def _deserialize(self, params):
        if params.get("CacheRules") is not None:
            self.CacheRules = []
            for item in params.get("CacheRules"):
                obj = SimpleCacheRule()
                obj._deserialize(item)
                self.CacheRules.append(obj)
        self.FollowOrigin = params.get("FollowOrigin")
        self.IgnoreCacheControl = params.get("IgnoreCacheControl")
        self.IgnoreSetCookie = params.get("IgnoreSetCookie")
        self.CompareMaxAge = params.get("CompareMaxAge")


class SimpleCacheRule(AbstractModel):
    """Cache expiration rules configuration

    """

    def __init__(self):
        """
        :param CacheType: Rule types:
all: all files take effect
file: specified file suffixes take effect
directory: specified paths take effect
path: specified absolute paths take effect
index: home page
        :type CacheType: str
        :param CacheContents: Matching content under the corresponding types for CacheType
For "all", enter an asterisk (*).
For "file", enter the suffix, such as jpg, txt.
For "directory", enter the path, such as /xxx/test/.
For "path", enter the corresponding absolute path, such as /xxx/test.html.
For "index", enter a backslash (/).
        :type CacheContents: list of str
        :param CacheTime: Cache expiration time settings
Unit: second. The maximum value is 365 days.
        :type CacheTime: int
        """
        self.CacheType = None
        self.CacheContents = None
        self.CacheTime = None


    def _deserialize(self, params):
        self.CacheType = params.get("CacheType")
        self.CacheContents = params.get("CacheContents")
        self.CacheTime = params.get("CacheTime")


class Sort(AbstractModel):
    """Query result sorting conditions

    """

    def __init__(self):
        """
        :param Key: Sorting field, which currently supports:
createTime, domain name creation time.
certExpireTime, certificate expiration time.
        :type Key: str
        :param Sequence: asc/desc, which is desc by default.
        :type Sequence: str
        """
        self.Key = None
        self.Sequence = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Sequence = params.get("Sequence")


class SpecificConfig(AbstractModel):
    """Specific configuration for domain names inside and outside mainland China by regions.

    """

    def __init__(self):
        """
        :param Mainland: Specific configuration for domain name inside mainland China.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Mainland: :class:`tencentcloud.cdn.v20180606.models.MainlandConfig`
        :param Overseas: Specific configuration for domain name outside mainland China.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Overseas: :class:`tencentcloud.cdn.v20180606.models.OverseaConfig`
        """
        self.Mainland = None
        self.Overseas = None


    def _deserialize(self, params):
        if params.get("Mainland") is not None:
            self.Mainland = MainlandConfig()
            self.Mainland._deserialize(params.get("Mainland"))
        if params.get("Overseas") is not None:
            self.Overseas = OverseaConfig()
            self.Overseas._deserialize(params.get("Overseas"))


class StartCdnDomainRequest(AbstractModel):
    """StartCdnDomain request structure.

    """

    def __init__(self):
        """
        :param Domain: Domain name
The domain name status should be **Disabled**
        :type Domain: str
        """
        self.Domain = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")


class StartCdnDomainResponse(AbstractModel):
    """StartCdnDomain response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StatusCodeCache(AbstractModel):
    """Status code cache expiration configuration. 404 status codes are cached for 10 seconds by default

    """

    def __init__(self):
        """
        :param Switch: Status code cache expiration configuration switch
on: enabled
off: disabled
Note: this field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        :param CacheRules: Status code cache expiration rules details
Note: this field may return null, indicating that no valid values can be obtained.
        :type CacheRules: list of StatusCodeCacheRule
        """
        self.Switch = None
        self.CacheRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("CacheRules") is not None:
            self.CacheRules = []
            for item in params.get("CacheRules"):
                obj = StatusCodeCacheRule()
                obj._deserialize(item)
                self.CacheRules.append(obj)


class StatusCodeCacheRule(AbstractModel):
    """Status code cache expiration time rule configuration

    """

    def __init__(self):
        """
        :param StatusCode: HTTP status code
Supports 403 and 404 status codes
        :type StatusCode: str
        :param CacheTime: Status code cache expiration time (in seconds)
        :type CacheTime: int
        """
        self.StatusCode = None
        self.CacheTime = None


    def _deserialize(self, params):
        self.StatusCode = params.get("StatusCode")
        self.CacheTime = params.get("CacheTime")


class StopCdnDomainRequest(AbstractModel):
    """StopCdnDomain request structure.

    """

    def __init__(self):
        """
        :param Domain: Domain name
The domain name status should be **Enabled**
        :type Domain: str
        """
        self.Domain = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")


class StopCdnDomainResponse(AbstractModel):
    """StopCdnDomain response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SummarizedData(AbstractModel):
    """Aggregate values of details; each metric has different aggregation methods based on its characteristics

    """

    def __init__(self):
        """
        :param Name: Aggregation method, which can be:
sum: aggregate summation
max: maximum value; in bandwidth mode, the peak bandwidth is calculated based on the aggregate data with 5-minute granularity.
avg: average value
        :type Name: str
        :param Value: Aggregate data value
        :type Value: float
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class TimestampData(AbstractModel):
    """Timestamp and its corresponding value

    """

    def __init__(self):
        """
        :param Time: Statistical point in time in forward rounding mode
Taking the 5-minute granularity as an example, 13:35:00 indicates that the statistical interval is between 13:35:00 and 13:39:59.
        :type Time: str
        :param Value: Data value
        :type Value: float
        """
        self.Time = None
        self.Value = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Value = params.get("Value")


class TopData(AbstractModel):
    """Data structure of sorted data

    """

    def __init__(self):
        """
        :param Resource: Resource name, which is classified as follows based on different query conditions:
A specific domain name: This indicates the details of this domain name
multiDomains: This indicates the aggregate details of multiple domain names
Project ID: This displays the ID of the specifically queried project
all: This indicates the details at the account level
        :type Resource: str
        :param DetailData: Detailed sorting results
        :type DetailData: list of TopDetailData
        """
        self.Resource = None
        self.DetailData = None


    def _deserialize(self, params):
        self.Resource = params.get("Resource")
        if params.get("DetailData") is not None:
            self.DetailData = []
            for item in params.get("DetailData"):
                obj = TopDetailData()
                obj._deserialize(item)
                self.DetailData.append(obj)


class TopDetailData(AbstractModel):
    """Data structure of sorted data

    """

    def __init__(self):
        """
        :param Name: Datatype name
        :type Name: str
        :param Value: Data value
        :type Value: float
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class UpdateDomainConfigRequest(AbstractModel):
    """UpdateDomainConfig request structure.

    """

    def __init__(self):
        """
        :param Domain: Domain name
        :type Domain: str
        :param ProjectId: Project ID
        :type ProjectId: int
        :param Origin: Origin server configuration
        :type Origin: :class:`tencentcloud.cdn.v20180606.models.Origin`
        :param IpFilter: IP blacklist/whitelist configuration
        :type IpFilter: :class:`tencentcloud.cdn.v20180606.models.IpFilter`
        :param IpFreqLimit: IP access limit configuration
        :type IpFreqLimit: :class:`tencentcloud.cdn.v20180606.models.IpFreqLimit`
        :param StatusCodeCache: Status code cache configuration
        :type StatusCodeCache: :class:`tencentcloud.cdn.v20180606.models.StatusCodeCache`
        :param Compression: Smart compression configuration
        :type Compression: :class:`tencentcloud.cdn.v20180606.models.Compression`
        :param BandwidthAlert: Bandwidth cap configuration
        :type BandwidthAlert: :class:`tencentcloud.cdn.v20180606.models.BandwidthAlert`
        :param RangeOriginPull: Range origin-pull configuration
        :type RangeOriginPull: :class:`tencentcloud.cdn.v20180606.models.RangeOriginPull`
        :param FollowRedirect: 301/302 origin-pull follow-redirect configuration
        :type FollowRedirect: :class:`tencentcloud.cdn.v20180606.models.FollowRedirect`
        :param ErrorPage: Error code redirect configuration (This feature is in beta test and not fully available yet.)
        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ErrorPage`
        :param RequestHeader: Request header configuration
        :type RequestHeader: :class:`tencentcloud.cdn.v20180606.models.RequestHeader`
        :param ResponseHeader: Response header configuration
        :type ResponseHeader: :class:`tencentcloud.cdn.v20180606.models.ResponseHeader`
        :param DownstreamCapping: Download speed configuration
        :type DownstreamCapping: :class:`tencentcloud.cdn.v20180606.models.DownstreamCapping`
        :param CacheKey: Node cache key configuration
        :type CacheKey: :class:`tencentcloud.cdn.v20180606.models.CacheKey`
        :param ResponseHeaderCache: Header cache configuration
        :type ResponseHeaderCache: :class:`tencentcloud.cdn.v20180606.models.ResponseHeaderCache`
        :param VideoSeek: Video dragging configuration
        :type VideoSeek: :class:`tencentcloud.cdn.v20180606.models.VideoSeek`
        :param Cache: Cache expiration time configuration
        :type Cache: :class:`tencentcloud.cdn.v20180606.models.Cache`
        :param OriginPullOptimization: Cross-border linkage optimization configuration
        :type OriginPullOptimization: :class:`tencentcloud.cdn.v20180606.models.OriginPullOptimization`
        :param Https: HTTPS acceleration configuration
        :type Https: :class:`tencentcloud.cdn.v20180606.models.Https`
        :param Authentication: Timestamp hotlink protection configuration
        :type Authentication: :class:`tencentcloud.cdn.v20180606.models.Authentication`
        :param Seo: SEO configuration
        :type Seo: :class:`tencentcloud.cdn.v20180606.models.Seo`
        :param ForceRedirect: Access protocol forced redirect configuration
        :type ForceRedirect: :class:`tencentcloud.cdn.v20180606.models.ForceRedirect`
        :param Referer: Referer hotlink protection configuration
        :type Referer: :class:`tencentcloud.cdn.v20180606.models.Referer`
        :param MaxAge: Browser cache configuration (This feature is in beta test and not fully available yet.)
        :type MaxAge: :class:`tencentcloud.cdn.v20180606.models.MaxAge`
        :param ServiceType: Domain name service type
web: static acceleration
download: download acceleration
media: streaming media VOD acceleration
        :type ServiceType: str
        :param SpecificConfig: Specific configuration for region attributes
Applicable to use cases where the configuration of accelerating domain names inside mainland China is inconsistent with the configuration outside mainland China.
        :type SpecificConfig: :class:`tencentcloud.cdn.v20180606.models.SpecificConfig`
        :param Area: Domain name acceleration region
mainland: acceleration inside mainland China
overseas: acceleration outside mainland China
global: global acceleration
        :type Area: str
        """
        self.Domain = None
        self.ProjectId = None
        self.Origin = None
        self.IpFilter = None
        self.IpFreqLimit = None
        self.StatusCodeCache = None
        self.Compression = None
        self.BandwidthAlert = None
        self.RangeOriginPull = None
        self.FollowRedirect = None
        self.ErrorPage = None
        self.RequestHeader = None
        self.ResponseHeader = None
        self.DownstreamCapping = None
        self.CacheKey = None
        self.ResponseHeaderCache = None
        self.VideoSeek = None
        self.Cache = None
        self.OriginPullOptimization = None
        self.Https = None
        self.Authentication = None
        self.Seo = None
        self.ForceRedirect = None
        self.Referer = None
        self.MaxAge = None
        self.ServiceType = None
        self.SpecificConfig = None
        self.Area = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.ProjectId = params.get("ProjectId")
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        if params.get("IpFilter") is not None:
            self.IpFilter = IpFilter()
            self.IpFilter._deserialize(params.get("IpFilter"))
        if params.get("IpFreqLimit") is not None:
            self.IpFreqLimit = IpFreqLimit()
            self.IpFreqLimit._deserialize(params.get("IpFreqLimit"))
        if params.get("StatusCodeCache") is not None:
            self.StatusCodeCache = StatusCodeCache()
            self.StatusCodeCache._deserialize(params.get("StatusCodeCache"))
        if params.get("Compression") is not None:
            self.Compression = Compression()
            self.Compression._deserialize(params.get("Compression"))
        if params.get("BandwidthAlert") is not None:
            self.BandwidthAlert = BandwidthAlert()
            self.BandwidthAlert._deserialize(params.get("BandwidthAlert"))
        if params.get("RangeOriginPull") is not None:
            self.RangeOriginPull = RangeOriginPull()
            self.RangeOriginPull._deserialize(params.get("RangeOriginPull"))
        if params.get("FollowRedirect") is not None:
            self.FollowRedirect = FollowRedirect()
            self.FollowRedirect._deserialize(params.get("FollowRedirect"))
        if params.get("ErrorPage") is not None:
            self.ErrorPage = ErrorPage()
            self.ErrorPage._deserialize(params.get("ErrorPage"))
        if params.get("RequestHeader") is not None:
            self.RequestHeader = RequestHeader()
            self.RequestHeader._deserialize(params.get("RequestHeader"))
        if params.get("ResponseHeader") is not None:
            self.ResponseHeader = ResponseHeader()
            self.ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("DownstreamCapping") is not None:
            self.DownstreamCapping = DownstreamCapping()
            self.DownstreamCapping._deserialize(params.get("DownstreamCapping"))
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("ResponseHeaderCache") is not None:
            self.ResponseHeaderCache = ResponseHeaderCache()
            self.ResponseHeaderCache._deserialize(params.get("ResponseHeaderCache"))
        if params.get("VideoSeek") is not None:
            self.VideoSeek = VideoSeek()
            self.VideoSeek._deserialize(params.get("VideoSeek"))
        if params.get("Cache") is not None:
            self.Cache = Cache()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("OriginPullOptimization") is not None:
            self.OriginPullOptimization = OriginPullOptimization()
            self.OriginPullOptimization._deserialize(params.get("OriginPullOptimization"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        if params.get("Authentication") is not None:
            self.Authentication = Authentication()
            self.Authentication._deserialize(params.get("Authentication"))
        if params.get("Seo") is not None:
            self.Seo = Seo()
            self.Seo._deserialize(params.get("Seo"))
        if params.get("ForceRedirect") is not None:
            self.ForceRedirect = ForceRedirect()
            self.ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Referer") is not None:
            self.Referer = Referer()
            self.Referer._deserialize(params.get("Referer"))
        if params.get("MaxAge") is not None:
            self.MaxAge = MaxAge()
            self.MaxAge._deserialize(params.get("MaxAge"))
        self.ServiceType = params.get("ServiceType")
        if params.get("SpecificConfig") is not None:
            self.SpecificConfig = SpecificConfig()
            self.SpecificConfig._deserialize(params.get("SpecificConfig"))
        self.Area = params.get("Area")


class UpdateDomainConfigResponse(AbstractModel):
    """UpdateDomainConfig response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdatePayTypeRequest(AbstractModel):
    """UpdatePayType request structure.

    """

    def __init__(self):
        """
        :param Area: Billing region, which can be mainland or overseas.
        :type Area: str
        :param PayType: Billing mode, which can be flux or bandwidth.
        :type PayType: str
        """
        self.Area = None
        self.PayType = None


    def _deserialize(self, params):
        self.Area = params.get("Area")
        self.PayType = params.get("PayType")


class UpdatePayTypeResponse(AbstractModel):
    """UpdatePayType response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UrlRecord(AbstractModel):
    """Details of the blocked URLs

    """

    def __init__(self):
        """
        :param Status: Status (disable: blocked; enable: unblocked)
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param RealUrl: Corresponding URL
Note: This field may return null, indicating that no valid values can be obtained.
        :type RealUrl: str
        :param CreateTime: Creation time
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param UpdateTime: Update time
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        """
        self.Status = None
        self.RealUrl = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RealUrl = params.get("RealUrl")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class VideoSeek(AbstractModel):
    """Video dragging configuration. It is disabled by default.

    """

    def __init__(self):
        """
        :param Switch: Video dragging switch
on: enabled
off: disabled
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class ViolationUrl(AbstractModel):
    """Details of violating URLs

    """

    def __init__(self):
        """
        :param Id: ID
        :type Id: int
        :param RealUrl: Origin access URL for violating resources
        :type RealUrl: str
        :param DownloadUrl: Snapshot path, which is used in the console to show the violating content snapshot.
        :type DownloadUrl: str
        :param UrlStatus: Current status of violating resources
forbid: blocked
release: unblocked
delay: handling delayed
reject: appeal dismissed. The status is still blocked.
complain: appeal in process
        :type UrlStatus: str
        :param CreateTime: Creation time
        :type CreateTime: str
        :param UpdateTime: Update time
        :type UpdateTime: str
        """
        self.Id = None
        self.RealUrl = None
        self.DownloadUrl = None
        self.UrlStatus = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.RealUrl = params.get("RealUrl")
        self.DownloadUrl = params.get("DownloadUrl")
        self.UrlStatus = params.get("UrlStatus")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")