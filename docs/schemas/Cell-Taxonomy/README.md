

<!-- schema-properties-start -->
## Schema properties
*Auto-generated from CSV. Do not edit this section manually.*

**Related LinkML model:** [Cell Taxonomy Model](https://brain-bican.github.io/models/index_cell_taxonomy/)

### Properties

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`accession_id`](#accession_id) | string | yes | — | A provider-assigned accession identifier for a given entity. |
| [`order`](#order) | integer | no | — | The priority or display order of an entity among all other entities of the same type. |

#### Abbreviation

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`id`](#id) | string | yes | — | Unique identifier for this abbreviation entry. |
| [`term`](#term) | string | yes | — | An abbreviation term as it appears in a cell type or cell set name. |
| [`meaning`](#meaning) | string | yes | — | The decoded meaning of the abbreviation term. |
| [`entity_type`](#entity_type) | AbbreviationEntityType | yes | — | The entity type which the abbreviation term denotes. |

#### Cell

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`id`](#id) | string | yes | — | Unique identifier for each individual cell. |
| [`cluster_id`](#cluster_id) | string | yes | — | Human-readable cluster label for the cluster assigned to this cell at a given annotation level. |
| [`load_id`](#load_id) | string | no | — | Identifier for the sequencing library from which molecular measurements were derived. |
| [`assay`](#assay) | string | no | — | Human-readable sequencing modality (e.g. 10x 3&#x27; v3). |
| [`assay_ontology_term_id`](#assay_ontology_term_id) | string | no | — | EFO ontology term for assay (e.g. EFO:0009922 for 10x 3&#x27; v3). |
| [`anatomical_region`](#anatomical_region) | string | no | — | Human-readable name for the anatomical region from which the cell was collected. |
| [`anatomical_region_ontology_term_id`](#anatomical_region_ontology_term_id) | string | no | — | UBERON ontology term for anatomical region (e.g. UBERON:0000955 for brain). |
| [`brain_region_ontology_term_id`](#brain_region_ontology_term_id) | string | no | — | Brain atlas region ID from DHBA/HBA/MBA for the anatomical region. |
| [`suspension_type`](#suspension_type) | SuspensionType | yes | — | Whether the measurement was performed on intact cells, nuclei, or is not applicable. |
| [`is_primary_data`](#is_primary_data) | boolean | yes | — | True if this is the canonical instance of this cellular observation; False for reanalysis or secondary views. |

#### CellTypeSet

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`id`](#id) | string | yes | — | Unique identifier for this annotation level. |
| [`name`](#name) | string | yes | — | Name of this annotation level used as column header in obs (e.g. Class, Subclass). |
| [`order`](#order) | integer | no | — | Integer rank of this annotation level in the hierarchy; lower values are broader types. |
| [`cell_type_set_type`](#cell_type_set_type) | CellTypeSetType | yes | — | A tag denoting whether this grouping represents a taxonomic level or neighborhood. |
| [`has_abbreviation`](#has_abbreviation) | Abbreviation | no | — | One of potentially many abbreviations that are part of the cell type set name. |

#### CellTypeTaxon

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`id`](#id) | string | yes | — | Unique identifier for this cell type taxon. |
| [`name`](#name) | string | yes | — | Human-readable label for this cell type taxon at the given annotation level (e.g. Glutamatergic). |
| [`accession_id`](#accession_id) | string | yes | — | Stable cross-version identifier for this cell type taxon (e.g. CS20230722_CLAS_11). |
| [`order`](#order) | integer | no | — | The priority or display order of this taxon among all taxons in the taxonomy. |
| [`cell_type_ontology_term`](#cell_type_ontology_term) | string | no | cell_type_ontology_term_id | CL ontology term for this cell type; use CL:0000003 for native cell if unknown. |
| [`number_of_cells`](#number_of_cells) | integer | yes | — | The aggregated number of cells that defines this cell type taxon. |
| [`has_abbreviation`](#has_abbreviation) | Abbreviation | no | — | One of potentially many abbreviations that are part of the cell type taxon name. |

#### CellTypeTaxonomy

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`id`](#id) | string | yes | — | Unique identifier for this taxonomy. |
| [`title`](#title) | string | yes | name | Description differentiating this taxonomy from others in the same collection; should be unique within a collection. |
| [`accession_id`](#accession_id) | string | yes | — | Provider-assigned accession identifier for this taxonomy (e.g. CCN20230722). |
| [`schema_version`](#schema_version) | string | yes | — | Version of the AIT schema used to produce this file (e.g. 1.0.0). |
| [`content_url`](#content_url) | uri | no | dataset_purl | Permanent URL to molecular data if the expression matrix is not embedded in the file. |
| [`batch_condition`](#batch_condition) | string | no | — | Cell metadata key(s) in obs that define batches for normalization or integration. |
| [`dendrogram`](#dendrogram) | string | no | — | JSON-formatted hierarchical clustering dendrogram encoding the taxonomy hierarchy. |
| [`hierarchy`](#hierarchy) | string | yes | — | Ordered mapping of annotation level names to integer ranks; lower rank means broader type. |
| [`mode`](#mode) | string | no | — | Active taxonomy mode controlling which subset of cells and analysis components to use. |
| [`filter`](#filter) | boolean | no | — | Per-mode boolean flags indicating cells to exclude (True means exclude). |
| [`cluster_algorithm`](#cluster_algorithm) | string | no | — | Full description of clustering algorithm and parameters used to produce cluster assignments. |
| [`cluster_info`](#cluster_info) | string | no | — | Summary table of cluster-level metadata including cluster sizes and representative metadata. |
| [`default_embedding`](#default_embedding) | string | no | — | Key in obsm of the embedding to display by default; must match an X_-prefixed entry. |
| [`cellannotation_schema`](#cellannotation_schema) | string | no | — | CAS annotation schema stored as JSON encoding labelset and annotation metadata. |
| [`quality_control_markers`](#quality_control_markers) | string | no | quality_control_markers | Marker gene expression data for patchseq quality control analysis. |
| [`reference_genome`](#reference_genome) | string | no | — | Reference genome assembly used to align the molecular measurements. |
| [`gene_annotation_version`](#gene_annotation_version) | string | no | — | Genome annotation version used during alignment. |

#### Cluster

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`id`](#id) | string | yes | — | Unique identifier for this cluster. |
| [`name`](#name) | string | yes | — | Human-readable label for this cluster; corresponds to cluster_id values in obs. |
| [`number_of_observations`](#number_of_observations) | integer | yes | — | Number of cells assigned to this cluster. |

#### ClusterSet

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`id`](#id) | string | yes | — | Unique identifier for this cluster set. |
| [`name`](#name) | string | no | — | Human-readable name for this cluster set (e.g. the name of the clustering run). |

#### ColorPalette

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`id`](#id) | string | yes | — | Unique identifier for this color palette. |
| [`name`](#name) | string | no | — | Name of the color palette. |
| [`description`](#description) | string | no | — | Description of the color palette. |

#### DisplayColor

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`id`](#id) | string | yes | — | Unique identifier for this display color entry. |
| [`color_hex_triplet`](#color_hex_triplet) | string | yes | — | A hex string representing the display color for an associated entity. |

#### Embedding

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`id`](#id) | string | yes | — | Unique identifier for this embedding. |
| [`embedding_key`](#embedding_key) | string | yes | — | Key used to store the embedding in obsm; must be prefixed with X_ (e.g. X_umap, X_pca). |
| [`embedding_matrix`](#embedding_matrix) | float | yes | — | N-dimensional matrix of shape n_cells × n_dims representing the low-dimensional projection. |

#### ExpressionMatrix

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`id`](#id) | string | yes | — | Unique identifier for this expression matrix. |
| [`matrix_type`](#matrix_type) | ExpressionMatrixType | yes | — | Whether this matrix contains normalized expression values or raw counts. |
| [`content_url`](#content_url) | uri | no | dataset_purl | URL to the matrix file if the matrix is not embedded directly in the h5ad file. |

### Property Details

<div id="accession_id" class="field-detail">
<h5><code>accession_id</code> <em>(required)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Subsets:</strong> uns</li>
</ul>
<p>A provider-assigned accession identifier for a given entity.</p>
</div>

<div id="order" class="field-detail">
<h5><code>order</code> <em>(optional)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>integer</code></li>
<li><strong>Subsets:</strong> uns</li>
</ul>
<p>The priority or display order of an entity among all other entities of the same type.</p>
</div>

#### Abbreviation

<div id="id" class="field-detail">
<h5><code>id</code> <em>(required)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Subsets:</strong> uns|annotations</li>
</ul>
<p>Unique identifier for this abbreviation entry.</p>
</div>

<div id="term" class="field-detail">
<h5><code>term</code> <em>(required)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Subsets:</strong> uns|annotations</li>
</ul>
<p>An abbreviation term as it appears in a cell type or cell set name.</p>
</div>

<div id="meaning" class="field-detail">
<h5><code>meaning</code> <em>(required)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Subsets:</strong> uns|annotations</li>
</ul>
<p>The decoded meaning of the abbreviation term.</p>
</div>

<div id="entity_type" class="field-detail">
<h5><code>entity_type</code> <em>(required)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>AbbreviationEntityType</code></li>
<li><strong>Subsets:</strong> uns|annotations</li>
</ul>
<p>The entity type which the abbreviation term denotes.</p>
<p><strong>Permissible values:</strong> <code>cell_type</code>, <code>gene</code>, <code>anatomical</code></p>
</div>

#### Cell

<div id="id" class="field-detail">
<h5><code>id</code> <em>(required)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Subsets:</strong> obs|assigned_metadata</li>
</ul>
<p>Unique identifier for each individual cell.</p>
</div>

<div id="cluster_id" class="field-detail">
<h5><code>cluster_id</code> <em>(required)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Subsets:</strong> obs|annotations</li>
</ul>
<p>Human-readable cluster label for the cluster assigned to this cell at a given annotation level.</p>
</div>

<div id="load_id" class="field-detail">
<h5><code>load_id</code> <em>(optional)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Subsets:</strong> obs|assigned_metadata</li>
</ul>
<p>Identifier for the sequencing library from which molecular measurements were derived.</p>
</div>

<div id="assay" class="field-detail">
<h5><code>assay</code> <em>(optional)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Subsets:</strong> obs|assigned_metadata</li>
</ul>
<p>Human-readable sequencing modality (e.g. 10x 3&#x27; v3).</p>
</div>

<div id="assay_ontology_term_id" class="field-detail">
<h5><code>assay_ontology_term_id</code> <em>(optional)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Subsets:</strong> obs|assigned_metadata</li>
</ul>
<p>EFO ontology term for assay (e.g. EFO:0009922 for 10x 3&#x27; v3).</p>
</div>

<div id="anatomical_region" class="field-detail">
<h5><code>anatomical_region</code> <em>(optional)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Subsets:</strong> obs|assigned_metadata</li>
</ul>
<p>Human-readable name for the anatomical region from which the cell was collected.</p>
</div>

<div id="anatomical_region_ontology_term_id" class="field-detail">
<h5><code>anatomical_region_ontology_term_id</code> <em>(optional)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Subsets:</strong> obs|assigned_metadata</li>
</ul>
<p>UBERON ontology term for anatomical region (e.g. UBERON:0000955 for brain).</p>
</div>

<div id="brain_region_ontology_term_id" class="field-detail">
<h5><code>brain_region_ontology_term_id</code> <em>(optional)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Subsets:</strong> obs|assigned_metadata</li>
</ul>
<p>Brain atlas region ID from DHBA/HBA/MBA for the anatomical region.</p>
</div>

<div id="suspension_type" class="field-detail">
<h5><code>suspension_type</code> <em>(required)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>SuspensionType</code></li>
<li><strong>Subsets:</strong> obs|assigned_metadata</li>
</ul>
<p>Whether the measurement was performed on intact cells, nuclei, or is not applicable.</p>
<p><strong>Permissible values:</strong> <code>cell</code>, <code>nucleus</code>, <code>na</code></p>
</div>

<div id="is_primary_data" class="field-detail">
<h5><code>is_primary_data</code> <em>(required)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>boolean</code></li>
<li><strong>Subsets:</strong> obs|assigned_metadata</li>
</ul>
<p>True if this is the canonical instance of this cellular observation; False for reanalysis or secondary views.</p>
</div>

#### CellTypeSet

<div id="id" class="field-detail">
<h5><code>id</code> <em>(required)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Subsets:</strong> uns|annotations</li>
</ul>
<p>Unique identifier for this annotation level.</p>
</div>

<div id="name" class="field-detail">
<h5><code>name</code> <em>(required)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Subsets:</strong> obs|uns|annotations</li>
</ul>
<p>Name of this annotation level used as column header in obs (e.g. Class, Subclass).</p>
</div>

<div id="order" class="field-detail">
<h5><code>order</code> <em>(optional)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>integer</code></li>
<li><strong>Subsets:</strong> uns|annotations</li>
</ul>
<p>Integer rank of this annotation level in the hierarchy; lower values are broader types.</p>
</div>

<div id="cell_type_set_type" class="field-detail">
<h5><code>cell_type_set_type</code> <em>(required)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>CellTypeSetType</code></li>
<li><strong>Subsets:</strong> uns|annotations</li>
</ul>
<p>A tag denoting whether this grouping represents a taxonomic level or neighborhood.</p>
<p><strong>Permissible values:</strong> <code>taxonomic_level</code>, <code>neighborhood</code></p>
</div>

<div id="has_abbreviation" class="field-detail">
<h5><code>has_abbreviation</code> <em>(optional)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>Abbreviation</code></li>
<li><strong>Subsets:</strong> uns|annotations</li>
</ul>
<p>One of potentially many abbreviations that are part of the cell type set name.</p>
</div>

#### CellTypeTaxon

<div id="id" class="field-detail">
<h5><code>id</code> <em>(required)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
</ul>
<p>Unique identifier for this cell type taxon.</p>
</div>

<div id="name" class="field-detail">
<h5><code>name</code> <em>(required)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Subsets:</strong> obs|annotations</li>
</ul>
<p>Human-readable label for this cell type taxon at the given annotation level (e.g. Glutamatergic).</p>
</div>

<div id="accession_id" class="field-detail">
<h5><code>accession_id</code> <em>(required)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Subsets:</strong> uns|annotations</li>
</ul>
<p>Stable cross-version identifier for this cell type taxon (e.g. CS20230722_CLAS_11).</p>
</div>

<div id="order" class="field-detail">
<h5><code>order</code> <em>(optional)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>integer</code></li>
<li><strong>Subsets:</strong> uns|annotations</li>
</ul>
<p>The priority or display order of this taxon among all taxons in the taxonomy.</p>
</div>

<div id="cell_type_ontology_term" class="field-detail">
<h5><code>cell_type_ontology_term</code> <em>(optional)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Aliases:</strong> cell_type_ontology_term_id</li>
<li><strong>Subsets:</strong> obs|annotations</li>
</ul>
<p>CL ontology term for this cell type; use CL:0000003 for native cell if unknown.</p>
</div>

<div id="number_of_cells" class="field-detail">
<h5><code>number_of_cells</code> <em>(required)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>integer</code></li>
<li><strong>Subsets:</strong> uns|annotations</li>
</ul>
<p>The aggregated number of cells that defines this cell type taxon.</p>
</div>

<div id="has_abbreviation" class="field-detail">
<h5><code>has_abbreviation</code> <em>(optional)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>Abbreviation</code></li>
<li><strong>Subsets:</strong> uns|annotations</li>
</ul>
<p>One of potentially many abbreviations that are part of the cell type taxon name.</p>
</div>

#### CellTypeTaxonomy

<div id="id" class="field-detail">
<h5><code>id</code> <em>(required)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
</ul>
<p>Unique identifier for this taxonomy.</p>
</div>

<div id="title" class="field-detail">
<h5><code>title</code> <em>(required)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Aliases:</strong> name</li>
<li><strong>Subsets:</strong> uns|tooling</li>
</ul>
<p>Description differentiating this taxonomy from others in the same collection; should be unique within a collection.</p>
</div>

<div id="accession_id" class="field-detail">
<h5><code>accession_id</code> <em>(required)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
</ul>
<p>Provider-assigned accession identifier for this taxonomy (e.g. CCN20230722).</p>
</div>

<div id="schema_version" class="field-detail">
<h5><code>schema_version</code> <em>(required)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Subsets:</strong> uns|tooling</li>
</ul>
<p>Version of the AIT schema used to produce this file (e.g. 1.0.0).</p>
</div>

<div id="content_url" class="field-detail">
<h5><code>content_url</code> <em>(optional)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>uri</code></li>
<li><strong>Aliases:</strong> dataset_purl</li>
<li><strong>Subsets:</strong> uns|data</li>
</ul>
<p>Permanent URL to molecular data if the expression matrix is not embedded in the file.</p>
</div>

<div id="batch_condition" class="field-detail">
<h5><code>batch_condition</code> <em>(optional)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Subsets:</strong> uns|tooling</li>
</ul>
<p>Cell metadata key(s) in obs that define batches for normalization or integration.</p>
</div>

<div id="dendrogram" class="field-detail">
<h5><code>dendrogram</code> <em>(optional)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Subsets:</strong> uns|annotations</li>
</ul>
<p>JSON-formatted hierarchical clustering dendrogram encoding the taxonomy hierarchy.</p>
</div>

<div id="hierarchy" class="field-detail">
<h5><code>hierarchy</code> <em>(required)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Subsets:</strong> uns|annotations</li>
</ul>
<p>Ordered mapping of annotation level names to integer ranks; lower rank means broader type.</p>
</div>

<div id="mode" class="field-detail">
<h5><code>mode</code> <em>(optional)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Subsets:</strong> uns|tooling</li>
</ul>
<p>Active taxonomy mode controlling which subset of cells and analysis components to use.</p>
</div>

<div id="filter" class="field-detail">
<h5><code>filter</code> <em>(optional)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>boolean</code></li>
<li><strong>Subsets:</strong> uns|tooling</li>
</ul>
<p>Per-mode boolean flags indicating cells to exclude (True means exclude).</p>
</div>

<div id="cluster_algorithm" class="field-detail">
<h5><code>cluster_algorithm</code> <em>(optional)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Subsets:</strong> uns|tooling</li>
</ul>
<p>Full description of clustering algorithm and parameters used to produce cluster assignments.</p>
</div>

<div id="cluster_info" class="field-detail">
<h5><code>cluster_info</code> <em>(optional)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Subsets:</strong> uns|annotations</li>
</ul>
<p>Summary table of cluster-level metadata including cluster sizes and representative metadata.</p>
</div>

<div id="default_embedding" class="field-detail">
<h5><code>default_embedding</code> <em>(optional)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Subsets:</strong> uns|tooling</li>
</ul>
<p>Key in obsm of the embedding to display by default; must match an X_-prefixed entry.</p>
</div>

<div id="cellannotation_schema" class="field-detail">
<h5><code>cellannotation_schema</code> <em>(optional)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Subsets:</strong> uns|tooling</li>
</ul>
<p>CAS annotation schema stored as JSON encoding labelset and annotation metadata.</p>
</div>

<div id="quality_control_markers" class="field-detail">
<h5><code>quality_control_markers</code> <em>(optional)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Aliases:</strong> quality_control_markers</li>
<li><strong>Subsets:</strong> uns|analysis</li>
</ul>
<p>Marker gene expression data for patchseq quality control analysis.</p>
</div>

<div id="reference_genome" class="field-detail">
<h5><code>reference_genome</code> <em>(optional)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Subsets:</strong> uns|assigned_metadata</li>
</ul>
<p>Reference genome assembly used to align the molecular measurements.</p>
</div>

<div id="gene_annotation_version" class="field-detail">
<h5><code>gene_annotation_version</code> <em>(optional)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Subsets:</strong> uns|assigned_metadata</li>
</ul>
<p>Genome annotation version used during alignment.</p>
</div>

#### Cluster

<div id="id" class="field-detail">
<h5><code>id</code> <em>(required)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Subsets:</strong> obs|uns|annotations</li>
</ul>
<p>Unique identifier for this cluster.</p>
</div>

<div id="name" class="field-detail">
<h5><code>name</code> <em>(required)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Subsets:</strong> obs|uns|annotations</li>
</ul>
<p>Human-readable label for this cluster; corresponds to cluster_id values in obs.</p>
</div>

<div id="number_of_observations" class="field-detail">
<h5><code>number_of_observations</code> <em>(required)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>integer</code></li>
<li><strong>Subsets:</strong> uns|annotations</li>
</ul>
<p>Number of cells assigned to this cluster.</p>
</div>

#### ClusterSet

<div id="id" class="field-detail">
<h5><code>id</code> <em>(required)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Subsets:</strong> uns|annotations</li>
</ul>
<p>Unique identifier for this cluster set.</p>
</div>

<div id="name" class="field-detail">
<h5><code>name</code> <em>(optional)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Subsets:</strong> uns|annotations</li>
</ul>
<p>Human-readable name for this cluster set (e.g. the name of the clustering run).</p>
</div>

#### ColorPalette

<div id="id" class="field-detail">
<h5><code>id</code> <em>(required)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Subsets:</strong> uns|tooling</li>
</ul>
<p>Unique identifier for this color palette.</p>
</div>

<div id="name" class="field-detail">
<h5><code>name</code> <em>(optional)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Subsets:</strong> uns|tooling</li>
</ul>
<p>Name of the color palette.</p>
</div>

<div id="description" class="field-detail">
<h5><code>description</code> <em>(optional)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Subsets:</strong> uns|tooling</li>
</ul>
<p>Description of the color palette.</p>
</div>

#### DisplayColor

<div id="id" class="field-detail">
<h5><code>id</code> <em>(required)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Subsets:</strong> uns|tooling</li>
</ul>
<p>Unique identifier for this display color entry.</p>
</div>

<div id="color_hex_triplet" class="field-detail">
<h5><code>color_hex_triplet</code> <em>(required)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Subsets:</strong> uns|tooling</li>
</ul>
<p>A hex string representing the display color for an associated entity.</p>
</div>

#### Embedding

<div id="id" class="field-detail">
<h5><code>id</code> <em>(required)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
</ul>
<p>Unique identifier for this embedding.</p>
</div>

<div id="embedding_key" class="field-detail">
<h5><code>embedding_key</code> <em>(required)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
<li><strong>Subsets:</strong> obsm|analysis</li>
</ul>
<p>Key used to store the embedding in obsm; must be prefixed with X_ (e.g. X_umap, X_pca).</p>
</div>

<div id="embedding_matrix" class="field-detail">
<h5><code>embedding_matrix</code> <em>(required)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>float</code></li>
<li><strong>Subsets:</strong> obsm|analysis</li>
</ul>
<p>N-dimensional matrix of shape n_cells × n_dims representing the low-dimensional projection.</p>
</div>

#### ExpressionMatrix

<div id="id" class="field-detail">
<h5><code>id</code> <em>(required)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>string</code></li>
</ul>
<p>Unique identifier for this expression matrix.</p>
</div>

<div id="matrix_type" class="field-detail">
<h5><code>matrix_type</code> <em>(required)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>ExpressionMatrixType</code></li>
<li><strong>Subsets:</strong> X|raw|data</li>
</ul>
<p>Whether this matrix contains normalized expression values or raw counts.</p>
<p><strong>Permissible values:</strong> <code>normalized</code>, <code>raw_count</code></p>
</div>

<div id="content_url" class="field-detail">
<h5><code>content_url</code> <em>(optional)</em></h5>
<ul>
<li><strong>Data Type:</strong> <code>uri</code></li>
<li><strong>Aliases:</strong> dataset_purl</li>
<li><strong>Subsets:</strong> uns|data</li>
</ul>
<p>URL to the matrix file if the matrix is not embedded directly in the h5ad file.</p>
</div>

<!-- schema-properties-end -->
