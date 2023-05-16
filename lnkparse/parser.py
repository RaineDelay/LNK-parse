# I'm planning on adding the print statements after, not sure if I should do that as
# the file is parsed or if I should save the results and format the printing later.

results = {}


def extract(filepath):
    with open(filepath, "rb") as fd:
        header_size = int.from_bytes(fd.read(4), "little")
        print(header_size)
        results["header_size"] = header_size
        CLSID = fd.read(
            16
        )  # write the check and formatting later probably save as a string
        set_flags = get_flags(
            fd.read(4)
        )  # flags in this list are true, any other flag is inherently false
        set_attrs = get_attributes(
            fd.read(4)
        )  # same as flags but with the file's attributes instead


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
        if (byte_arr[i // 8] & (1 << (7 - (i % 8)))) > 0
    ]
    print(set_flags)
    return set_flags


def get_attributes(byte_arr):
    print("hello attributes")
