
results = {}
def extract(fd):
    with open(fd, "rb"):
        header_size = int.from_bytes(fd.read(4), "little")
        results["header_size"] = header_size


def get_flags(byte_arr):
    #floor divide index of flags in dict to find byte
    #modulo 8 to find the bit 
    #do this with a dict comprehension
    flag_list = ["HasLinkTargetIDList", "HasLinkInfo", "HasName", "HasRelativePath", "HasWorkingDir",
                 "HasArguments", "HasIconLocation", "IsUnicode", "ForceNoLinkIfor", "HasExpString",
                 "RunInSeparateProcess", "Unused1", "HasDarwinID", "RunAsUser", "HasExpIcon", "NoPidAlias",
                 "Unused2", "RunWithShimLayer", "ForceNoLinkTrack", "EnableTargetMetadata",
                 "DisableLinkPathTracking", "DisableKnownFolderTracking", "DisableKnownFolderAlias",
                 "AllowLinkToLink", "UnaliasOnSave", "PreferEnivronmentPath", "KeepLocalIDListForUNCTarget"
                ]

