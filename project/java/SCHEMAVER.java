package None;

import java.util.List;
import lombok.*;



/* version: 0.3.0.post26.dev0+e73dc8d */


/**
  The data element in the handle API for the schema version.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SCHEMAVER extends HandleRecord {

  private int index;
  private HdlDataSchemaVer data;

}
