package None;

import java.util.List;
import lombok.*;



/* version: 0.3.0.post26.dev0+e73dc8d */


/**
  A container for all HandleRecords.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class HandleRecordContainer  {

  private List<HandleAPIRecord> containsPids;

}
