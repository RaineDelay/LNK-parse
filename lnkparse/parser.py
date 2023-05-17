import struct
from datetime import datetime

utc_start = datetime.fromisoformat("1970-01-01")
results = {}

# extract(filepath) is the primary function which calls every other individual function.
# it handles the file IO and simply prints what the other functions calculate
# along with adding those calcs to the results dictionary


def extract(filepath):
    with open(filepath, "rb") as fd:
        header_size = int.from_bytes(fd.read(4), "little")
        print(header_size)
        results["header_size"] = header_size
        CLSID = fd.read(
            16
        )  # write the check and formatting later probably save as a string
        print(CLSID)
        set_flags = get_flags(
            fd.read(4)
        )  # flags in this list are true, any other flag is inherently false
        print(set_flags)
        set_attrs = get_attributes(
            fd.read(4)
        )  # same as flags but with the file's attributes instead
        print(set_attrs)
        results["Creation Time"] = time_calc(fd.read(8))
        print("Creation Time: {}".format(results["Creation Time"]))
        results["Access Time"] = time_calc(fd.read(8))
        print("Access Time: {}".format(results["Access Time"]))
        results["Write Time"] = time_calc(fd.read(8))
        print("Write Time: {}".format(results["Write Time"]))


# get_flags takes a byte array of exactly four bytes, then performs a bitmask over these
# bytes to determine which are set.


def get_flags(byte_arr):
    # floor divide index of flags in dict to find byte
    # modulo 8 to find the bit
    # do this with a dict comprehension
    flag_list = [
        "HasLinkTargetIDList",
        "HasLinkInfo",
        "HasName",
        "HasRelativePath",
        "HasWorkingDir",
        "HasArguments",
        "HasIconLocation",
        "IsUnicode",
        "ForceNoLinkIfor",
        "HasExpString",
        "RunInSeparateProcess",
        "Unused1",
        "HasDarwinID",
        "RunAsUser",
        "HasExpIcon",
        "NoPidAlias",
        "Unused2",
        "RunWithShimLayer",
        "ForceNoLinkTrack",
        "EnableTargetMetadata",
        "DisableLinkPathTracking",
        "DisableKnownFolderTracking",
        "DisableKnownFolderAlias",
        "AllowLinkToLink",
        "UnaliasOnSave",
        "PreferEnivronmentPath",
        "KeepLocalIDListForUNCTarget",
    ]
    set_flags = [
        flag
        for i, flag in enumerate(flag_list)
        if (byte_arr[i // 8] & (1 << (i % 8))) > 0
    ]
    return set_flags


# get_attributes is the same process as get_flags but with a different list


def get_attributes(byte_arr):
    attr_list = [
        "FILE_ATTRIBUTE_READONLY",
        "FILE_ATTRIBUTE_HIDDEN",
        "FILE_ATTRIBUTE_SYSTEM",
        "Reserved1",
        "FILE_ATTRIBUTE_DIRECTORY",
        "FILE_ATTRIBUTE_ARCHIVE",
        "Reserved2",
        "FILE_ATTRIBUTE_NORMAL",
        "FILE_ATTRIBUTE_TEMPORARY",
        "FILE_ATTRIBUTE_SPARSE_FILE",
        "FILE_ATTRIBUTE_REPARSE_POINT",
        "FILE_ATTRIBUTE_COMPRESSED",
        "FILE_ATTRIBUTE_OFFLINE",
        "FILE_ATTRIBUTE_NOT_CONTENT_INDEXED",
        "FILE_ATTRIBUTE_ENCRYPTED",
    ]
    set_attrs = [
        attr
        for i, attr in enumerate(attr_list)
        if (byte_arr[i // 8] & (1 << (i % 8))) > 0
    ]
    return set_attrs


# time_calc takes a byte array of size 8, unpacks to a long long, then subtract
# the difference between the Windows epoch and the Linux epoch


def time_calc(byte_arr):
    micro = struct.unpack("<q", byte_arr)[0]
    result = datetime.fromtimestamp(micro / 10000000.0 - 11644473600).strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    # the following was a failed attempt
    # seconds = int.from_bytes(byte_arr, "little", signed="False") / 100000000
    # print(micro)
    # delta = timedelta(seconds=seconds)
    # print(delta)
    # print(utc_start + delta)
    # return utc_start + delta
    return result
