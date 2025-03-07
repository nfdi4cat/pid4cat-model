package None;

import java.util.List;
import lombok.*;



/* version: 0.0.0 */


/**
  The data element in the handle API for the schema version.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SCHEMAVER extends HandleRecord {

  private int index;
  private HdlDataSchemaVer data;

}
