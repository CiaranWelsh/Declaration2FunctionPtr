import os
import re

definitions = """
_GraphfabExport void gf_freeSBMLModel(gf_SBMLModel* lo);
_GraphfabExport gf_SBMLModel* gf_loadSBMLbuf(const char* buf);
_GraphfabExport gf_SBMLModel* gf_loadSBMLfile(const char* file);
_GraphfabExport void gf_freeLayoutInfo(gf_layoutInfo* l);
_GraphfabExport void gf_freeLayoutInfoHierarch(gf_layoutInfo* l);
_GraphfabExport void gf_freeModelAndLayout(gf_SBMLModel* mod, gf_layoutInfo* l);
_GraphfabExport gf_SBMLModel gf_SBMLModel_new();
_GraphfabExport gf_SBMLModel* gf_SBMLModel_newp();
_GraphfabExport gf_layoutInfo gf_layoutInfo_new(uint64_t level, uint64_t version, uint64_t width, uint64_t height);
_GraphfabExport gf_layoutInfo* gf_layoutInfo_newp(uint64_t level, uint64_t version, uint64_t width, uint64_t height);
_GraphfabExport gf_layoutInfo* gf_processLayout(gf_SBMLModel* lo);
_GraphfabExport gf_layoutInfo* gf_loadSBMLIntoLayoutEngine(const char* buf, gf_SBMLModel* r);
_GraphfabExport void gf_setModelNamespace(gf_layoutInfo* l, unsigned long level, unsigned long version);
_GraphfabExport const char* gf_getDefaultCompartmentId();
_GraphfabExport void gf_setDefaultCompartmentId(const char* id);
_GraphfabExport gf_network gf_getNetwork(gf_layoutInfo* l);
_GraphfabExport gf_network* gf_getNetworkp(gf_layoutInfo* l);
_GraphfabExport void gf_clearNetwork(gf_network* n);
_GraphfabExport void gf_releaseNetwork(gf_network* n);
_GraphfabExport char* gf_nw_getId(gf_network* n);
_GraphfabExport void gf_nw_setId(gf_network* n, const char* id);
_GraphfabExport uint64_t gf_nw_getNumNodes(const gf_network* n);
_GraphfabExport uint64_t gf_nw_getNumUniqueNodes(const gf_network* n);
_GraphfabExport uint64_t gf_nw_getNumRxns(const gf_network* n);
_GraphfabExport uint64_t gf_nw_getNumComps(const gf_network* n);
_GraphfabExport gf_node gf_nw_getNode(gf_network* n, uint64_t i);
_GraphfabExport gf_node gf_nw_getUniqueNode(gf_network* n, uint64_t i);
_GraphfabExport gf_node* gf_nw_getNodep(gf_network* n, uint64_t i);
_GraphfabExport gf_node* gf_nw_getUniqueNodep(gf_network* n, uint64_t i);
_GraphfabExport gf_node* gf_nw_getNodepFromId(gf_network* nw, const char* id);
_GraphfabExport gf_reaction gf_nw_getRxn(gf_network* n, uint64_t i);
_GraphfabExport gf_reaction* gf_nw_getRxnp(gf_network* n, uint64_t i);
_GraphfabExport void gf_nw_removeRxn(gf_network* n, gf_reaction* r);
_GraphfabExport gf_compartment gf_nw_getCompartment(gf_network* n, uint64_t i);
_GraphfabExport gf_compartment* gf_nw_getCompartmentp(gf_network* n, uint64_t i);
_GraphfabExport gf_compartment* gf_nw_findCompartmentById(gf_network* n, const char* id);
_GraphfabExport void gf_nw_rebuildCurves(gf_network* n);
_GraphfabExport void gf_nw_recenterJunctions(gf_network* n);
_GraphfabExport gf_compartment gf_nw_newCompartment(gf_network* nw, const char* id, const char* name);
_GraphfabExport gf_compartment* gf_nw_newCompartmentp(gf_network* nw, const char* id, const char* name);
_GraphfabExport gf_node gf_nw_newNode(gf_network* nw, const char* id, const char* name, gf_compartment* compartment);
_GraphfabExport gf_node gf_nw_aliasOf(gf_network* nw, gf_node* n);
_GraphfabExport gf_node* gf_nw_newNodep(gf_network* nw, const char* id, const char* name, gf_compartment* compartment);
_GraphfabExport gf_node* gf_nw_newAliasNodep(gf_network* nw, gf_node* source);
_GraphfabExport int gf_nw_removeNode(gf_network* nw, gf_node* node);
_GraphfabExport int gf_nw_connectNode(gf_network* nw, gf_node* node, gf_reaction* reaction, gf_specRole role);
_GraphfabExport int gf_nw_connectNodeRoleStr(gf_network* nw, gf_node* n, gf_reaction* r, const char* role_str);
_GraphfabExport int gf_nw_isNodeConnected(gf_network* nw, gf_node* node, gf_reaction* reaction);
_GraphfabExport int gf_nw_isLayoutSpecified(gf_network* nw);
_GraphfabExport int gf_nw_getNumInstances(gf_network* nw, gf_node* n);
_GraphfabExport int gf_nw_getNumAliasInstances(gf_network* nw, gf_node* n);
_GraphfabExport gf_node gf_nw_getInstance(gf_network* nw, gf_node* n, uint64_t i);
_GraphfabExport gf_node* gf_nw_getInstancep(gf_network* nw, gf_node* n, uint64_t i);
_GraphfabExport gf_node* gf_nw_getAliasInstancep(gf_network* nw, gf_node* n, uint64_t i);
_GraphfabExport void gf_node_setCompartment(gf_node* n, gf_compartment* c);
_GraphfabExport void gf_clearNode(gf_node* n);
_GraphfabExport void gf_releaseNode(const gf_node* n);
_GraphfabExport int gf_node_isLocked(gf_node* n);
_GraphfabExport void gf_node_lock(gf_node* n);
_GraphfabExport void gf_node_unlock(gf_node* n);
_GraphfabExport int gf_node_alias(gf_node* n, gf_network* m);
_GraphfabExport int gf_node_make_alias(gf_node* n, gf_network* m);
_GraphfabExport int gf_node_isAliased(gf_node* n);
_GraphfabExport void gf_node_setIsAlias(gf_node* n, int isAlias);
_GraphfabExport gf_point gf_node_getCentroid(gf_node* n);
_GraphfabExport void gf_node_getCentroidXY(gf_node* n, double* x, double* y);
_GraphfabExport void gf_node_setCentroid(gf_node* n, gf_point p);
_GraphfabExport double gf_node_getWidth(gf_node* n);
_GraphfabExport void gf_node_setWidth(gf_node* n, double width);
_GraphfabExport double gf_node_getHeight(gf_node* n);
_GraphfabExport void gf_node_setHeight(gf_node* n, double height);
_GraphfabExport char* gf_node_getID(gf_node* n);
_GraphfabExport void gf_node_setID(gf_node* n, const char* id);
_GraphfabExport const char* gf_node_getName(gf_node* n);
_GraphfabExport void gf_node_setName(gf_node* n, const char* name);
_GraphfabExport int gf_node_getConnectedReactions(gf_node* n, gf_network* m, unsigned int* num, gf_reaction** rxns);
_GraphfabExport int gf_node_getAttachedCurves(gf_node* n, gf_network* m, unsigned int* num, gf_curve** curves);
_GraphfabExport int gf_node_isIdentical(gf_node* u, gf_node* v);
_GraphfabExport int gf_nw_nodeHasCompartment(gf_network* nw, gf_node* x);
_GraphfabExport gf_compartment* gf_nw_nodeGetCompartment(gf_network* nw, gf_node* x);
_GraphfabExport void gf_releaseRxn(const gf_reaction* r);
_GraphfabExport gf_reaction gf_nw_newReaction(gf_network* nw, const char* id, const char* name);
_GraphfabExport gf_reaction* gf_nw_newReactionp(gf_network* nw, const char* id, const char* name);
_GraphfabExport char* gf_reaction_getID(gf_reaction* r);
_GraphfabExport gf_point gf_reaction_getCentroid(gf_reaction* r);
_GraphfabExport void gf_reaction_setCentroid(gf_reaction* r, gf_point p);
_GraphfabExport uint64_t gf_reaction_getNumSpec(const gf_reaction* r);
_GraphfabExport int gf_reaction_hasSpec(const gf_reaction* r, const gf_node* n);
_GraphfabExport gf_specRole gf_reaction_getSpecRole(const gf_reaction* r, uint64_t i);
_GraphfabExport const char* gf_roleToStr(gf_specRole role);
_GraphfabExport gf_specRole gf_strToRole(const char* str);
_GraphfabExport uint64_t gf_reaction_specGeti(const gf_reaction* r, uint64_t i);
_GraphfabExport uint64_t gf_reaction_getNumCurves(const gf_reaction* r);
_GraphfabExport gf_curve gf_reaction_getCurve(const gf_reaction* r, uint64_t i);
_GraphfabExport gf_curve* gf_reaction_getCurvep(const gf_reaction* r, uint64_t i);
_GraphfabExport void gf_reaction_recenter(gf_reaction* r);
_GraphfabExport void gf_reaction_recalcCurveCPs(gf_reaction* r);
_GraphfabExport void gf_releaseCurve(const gf_curve* c);
_GraphfabExport char* gf_curve_getID(gf_curve* c);
_GraphfabExport gf_specRole gf_curve_getRole(gf_curve* c);
_GraphfabExport gf_curveCP gf_getCurveCPs(const gf_curve* c);
_GraphfabExport int gf_curve_hasArrowhead(const gf_curve* c);
_GraphfabExport int gf_curve_getArrowheadVerts(const gf_curve* c, unsigned int* n, gf_point** v);
_GraphfabExport void gf_releaseCompartment(const gf_compartment* c);
_GraphfabExport char* gf_compartment_getID(gf_compartment* c);
_GraphfabExport gf_point gf_compartment_getMinCorner(gf_compartment* c);
_GraphfabExport void gf_compartment_setMinCorner(gf_compartment* c, gf_point p);
_GraphfabExport gf_point gf_compartment_getMaxCorner(gf_compartment* c);
_GraphfabExport void gf_compartment_setMaxCorner(gf_compartment* c, gf_point p);
_GraphfabExport double gf_compartment_getWidth(gf_compartment* c);
_GraphfabExport double gf_compartment_getHeight(gf_compartment* c);
_GraphfabExport uint64_t gf_compartment_getNumElt(gf_compartment* c);
_GraphfabExport int gf_compartment_addNode(gf_compartment* c, gf_node* n);
_GraphfabExport int gf_compartment_removeNode(gf_compartment* c, gf_node* n);
_GraphfabExport int gf_compartment_containsNode(gf_compartment* c, gf_node* n);
_GraphfabExport int gf_compartment_containsReaction(gf_compartment* c, gf_reaction* r);
_GraphfabExport void gf_fit_to_window(gf_layoutInfo* l, double left, double top, double right, double bottom);
_GraphfabExport gf_transform* gf_tf_fitToWindow(gf_layoutInfo* l, double left, double top, double right, double bottom);
_GraphfabExport void gf_moveNetworkToFirstQuad(gf_layoutInfo* l, double x_disp, double y_disp);
_GraphfabExport CPoint gf_tf_apply_to_point(gf_transform* tf, CPoint p);
_GraphfabExport gf_point gf_tf_getScale(gf_transform* tf);
_GraphfabExport gf_point gf_tf_getDisplacement(gf_transform* tf);
_GraphfabExport gf_point gf_tf_getPostDisplacement(gf_transform* tf);
_GraphfabExport void gf_dump_transform(gf_transform* tf);
_GraphfabExport void gf_release_transform(gf_transform* tf);
_GraphfabExport gf_canvas gf_getCanvas(gf_layoutInfo* l);
_GraphfabExport gf_canvas* gf_getCanvasp(gf_layoutInfo* l);
_GraphfabExport void gf_clearCanvas(gf_canvas* c);
_GraphfabExport void gf_releaseCanvas(gf_canvas* c);
_GraphfabExport unsigned int gf_canvGetWidth(gf_canvas* c);
_GraphfabExport unsigned int gf_canvGetHeight(gf_canvas* c);
_GraphfabExport void gf_canvSetWidth(gf_canvas* c, unsigned long width);
_GraphfabExport void gf_canvSetHeight(gf_canvas* c, unsigned long height);
_GraphfabExport void gf_getNodeCentroid(gf_layoutInfo* l, const char* id, CPoint* p);
_GraphfabExport int gf_lockNodeId(gf_layoutInfo* l, const char* id);
_GraphfabExport int gf_unlockNodeId(gf_layoutInfo* l, const char* id);
_GraphfabExport int gf_aliasNodeId(gf_layoutInfo* l, const char* id);
_GraphfabExport void gf_aliasNodebyDegree(gf_layoutInfo* l, const int minDegree);
_GraphfabExport void gf_randomizeLayout(gf_layoutInfo* m);
_GraphfabExport void gf_randomizeLayout2(gf_network* n, gf_canvas* c);
_GraphfabExport void gf_randomizeLayout_fromExtents(gf_network* n, double left, double top, double right, double bottom);
_GraphfabExport int gf_writeSBMLwithLayout(const char* filename, gf_SBMLModel* m, gf_layoutInfo* l);
_GraphfabExport int gf_writeSBML(const char* filename, gf_SBMLModel* m);
_GraphfabExport const char* gf_getSBMLwithLayoutStr(gf_SBMLModel* m, gf_layoutInfo* l);
_GraphfabExport const char* gf_getCurrentLibraryVersion(void);
_GraphfabExport void gf_free(void* x);
_GraphfabExport gf_point gf_computeCubicBezierPoint(gf_curveCP* c, Real t);
_GraphfabExport gf_point* gf_computeCubicBezierLineIntersec(gf_curveCP* c, gf_point* line_start, gf_point* line_end);
_GraphfabExport int gf_arrowheadStyleGetNumVerts(int style);
_GraphfabExport gf_point gf_arrowheadStyleGetVert(int style, int n);
_GraphfabExport int gf_arrowheadStyleIsFilled(int style);
_GraphfabExport unsigned long gf_arrowheadNumStyles();
_GraphfabExport void gf_arrowheadSetStyle(gf_specRole role, int style);
_GraphfabExport int gf_arrowheadGetStyle(gf_specRole role);
"""


class Declaration:

    def __init__(self, definition):
        self.decl = definition

    def get_exporter_symbol(self):
        match = re.findall('^\S*', self.decl)
        assert len(match) == 1
        return match[0]

    def get_return_type(self):
        match = re.findall('^\S*\s*(unsigned \S*)|^\S*\s*(const \S*)|^\S*\s*(\S*)', self.decl)
        assert len(match) == 1
        match = [i for i in match[0] if i != '']
        assert len(match) == 1
        return match[0]

    def get_method_name(self):
        match = re.findall('(?:^\S*\s*unsigned \S*|^\S*\s*const \S*|^\S*\s*)\S*\s*(\S*)(?=\()', self.decl)
        assert len(match) == 1
        return match[0]

    def get_arg_types(self):
        match = re.findall('(?:^\S*\s*unsigned \S*|^\S*\s*const \S*|^\S*\s*)\S*\s*\S*(?=\()\((.*)\);', self.decl)
        assert len(match) == 1
        print(match)
        matches = match[0].split(',')
        types = []
        for i in match:
            # remove the variable name from the string
            i = i.rsplit(' ')[:-1]
            i = ' '.join(i)
            match = re.findall('(const\s*\S*)|(unsigned\s*\S*)|(\S*)\s*\S*', i)
            match = [i for i in match if i != ('','','')]
            assert len(match) == 1
            types.append([i for i in match[0] if i != ''][0])
        return types
